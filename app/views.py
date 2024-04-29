from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import SignUpForm, CreateClientForm, CreatePetForm, DeleteForm
from .models import Client
from .models import Pet


# home page
def home(request):
    """
    Render the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered home page.

    """
    # grab client records
    clients = Client.objects.all()
    # check login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate info ^
        user = authenticate(request, username=username, password=password)
        # if all good, login
        if user is not None:
            login(request, user)
            # popup msg for confirmation
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.success(request, "Login Failed")
            return redirect('home')
    else:
        return render(request, 'home.html', {'clients':clients})

# logging out user
def logout_user(request):
    """
    Log out the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the home page after logging out.

    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# register/signup
def register_user(request):
    """
    Register a new user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse:
        The HTTP response object containing the registration form or a redirect to the home page.

    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # make sure form meets reqs
        if form.is_valid():
            user = form.save()  # Save the form and get the user object

            # Add user to the "Employee" group
            employee_group = Group.objects.get(name='Employee')
            employee_group.user_set.add(user)

            # get username / pass from form
            username = form.cleaned_data['username'] # pull username from form
            password = form.cleaned_data['password1'] # pull pass1
            # authenticate
            user = authenticate(username=username, password=password)
            # login
            login(request, user)
            messages.success(request, "You have successfully signed up!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


# view specific client info
def view_client(request, pk):
    """
    View detailed information about a client.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the client to view.

    Returns:
        HttpResponse: The HTTP response object containing the client's details and associated pets.

"""
    # get single client record
    client_record = Client.objects.get(id=pk)

    # get pets associated with client
    pets = Pet.objects.filter(owner=client_record)

    return render(request, 'view.html', {"client_record": client_record, "pets": pets})



# delete the specific client record
@login_required
def delete_client(request, pk):
    """
    Delete a client record.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the client to delete.

    Returns:
        HttpResponse:
        The HTTP response object containing the deletion confirmation
        or a redirect to the home page.
    """
    try:
        # check if the user has the 'delete_client' permission
        permission_required('app.delete_client', raise_exception=True)(request)

        # check if the user is in the 'Employee' group
        if request.user.groups.filter(name='Employee').exists():
            messages.error(request, "You do not have permission to delete a client.")
            return redirect(request.META.get('HTTP_REFERER', 'home'))

        # get client
        client = Client.objects.get(id=pk)
        form = DeleteForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                user = authenticate(username=request.user.username, password=password)

                if user is not None and confirm_password == password:
                    client.delete()
                    messages.success(request, "Client record has been deleted.")
                    return redirect('home')
                else:
                    messages.error(
                        request,
                        "Password authentication failed or passwords don't match.")

        return render(request, 'delete_client.html', {'client': client, 'form': form})

    except PermissionDenied:
        # if the user doesn't have permission, display error message and redirect
        messages.error(request, "You do not have permission to delete a client.")
        # redirect to the previous page or 'home' if no previous page
        return redirect(request.META.get('HTTP_REFERER', 'home'))

# create new client record
@login_required
def create_client(request):
    """
    Create a new client record.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse:
        The HTTP response object containing the client creation form or a redirect to the home page.
    """
    try:
        # check if the user has the 'add_client' permission
        permission_required('app.add_client', raise_exception=True)(request)

        # check if the user is in the 'Employee' group
        if request.user.groups.filter(name='Employee').exists():
            messages.error(request, "You do not have permission to create a new client.")
            return redirect(request.META.get('HTTP_REFERER', 'home'))

        if request.method == "POST":
            form = CreateClientForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Client created.")
                return redirect('home')
        else:
            form = CreateClientForm()

        return render(request, 'create.html', {'form': form})

    except PermissionDenied:
        # if the user doesn't have permission, display error message and redirect
        messages.error(request, "You do not have permission to create a new client.")
        # redirect to the previous page or 'home' if no previous page
        return redirect(request.META.get('HTTP_REFERER', 'home'))

# edit and update client record
@login_required
def edit_client(request, pk):
    """
    Edit an existing client record.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the client to edit.

    Returns:
        HttpResponse:
        The HTTP response object containing the client editing form or a redirect to the home page.
    """
    # get specific record by id
    current_record = Client.objects.get(id=pk)
    form = CreateClientForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Client updated.")
        return redirect('home')
    return render(request, 'edit.html', {'form': form})

# add pet for client
def add_pet(request, client_id):
    """
    Add a new pet for a client.

    Args:
        request (HttpRequest): The HTTP request object.
        client_id (int): The primary key of the client for whom to add a pet.

    Returns:
        HttpResponse:
        The HTTP response object containing the pet addition form
        or a redirect to the client's page.

    """
    # check if the user is logged in
    if request.user.is_authenticated:
        # get the client object based on the client_id
        client = Client.objects.get(id=client_id)

        if request.method == "POST":
            # create a form instance and populate it with data from the request
            form = CreatePetForm(request.POST, request.FILES)
            if form.is_valid():
                # create a pet instance but don't save it to the database yet
                pet = form.save(commit=False)
                # associate the pet with the client
                pet.owner = client
                # save the pet to the database
                pet.save()
                messages.success(request, "Pet added.")
                # redirect to the view client page after adding the pet
                return redirect('view', pk=client_id)
        else:
            # if it's a GET request, create an empty form
            form = CreatePetForm()

        # render the add pet form with the client information
        return render(request, 'add_pet.html', {'form': form, 'client': client})
    else:
        messages.error(request, "You must be logged in to add a pet.")
        return redirect('home')


# edit pet
def edit_pet(request, pk):
    """
    Edit an existing pet record.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the pet to edit.

    Returns:
        HttpResponse:
        The HTTP response object containing the pet editing form
        or a redirect to the client's page.

    """
    # check if logged in
    if request.user.is_authenticated:
        # get specific pet record
        pet = Pet.objects.get(id=pk)
        form = CreatePetForm(request.POST or None, request.FILES or None, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, "Pet information updated.")
            return redirect('view', pk=pet.owner.id)
        return render(request, 'edit_pet.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to edit.")
        return redirect('home')

# delete the specific pet record
def delete_pet(request, pk):
    """
    Delete a pet record.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the pet to delete.

    Returns:
        HttpResponse:
        The HTTP response object containing the deletion confirmation
        or a redirect to the home page.
    """
    # check if logged in
    if request.user.is_authenticated:
        # get pet
        pet = Pet.objects.get(id=pk)
        form = DeleteForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                user = authenticate(username=request.user.username, password=password)

                if user is not None and confirm_password == password:
                    pet.delete()
                    messages.success(request, "Pet record has been deleted.")
                    return redirect('view', pk=pet.owner.id)
                else:
                    messages.error(
                        request,
                        "Password authentication failed or passwords don't match.")

        return render(request, 'delete_pet.html', {'pet': pet, 'form': form})
    else:
        messages.success(request, "You must be logged in to view.")
        return redirect('home')