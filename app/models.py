from django.db import models

# model for client records
class Client(models.Model):
    """
    Model representing a client record.

    Attributes:
        created_at (DateTimeField): The date and time when the record was created.
        first_name (CharField): The first name of the client.
        last_name (CharField): The last name of the client.
        address (CharField): The address of the client.
        city (CharField): The city where the client resides.
        state (CharField): The state where the client resides.
        email (CharField): The email address of the client.
        phone_number (CharField): The phone number of the client.

    """
    # field for when record is created
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

# model for pet records
class Pet(models.Model):
    """
    Model representing a pet record.

    Attributes:
        name (CharField): The name of the pet.
        birthday (DateField): The birthday of the pet.
        sex (CharField): The sex of the pet.
        species (CharField): The species of the pet.
        breed (CharField): The breed of the pet.
        color (CharField): The color of the pet.
        owner (ForeignKey): The owner of the pet (a Client instance).
        pet_img (ImageField): An optional image of the pet.

    """

     # choices for sex
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]

    # choices for species
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other')
        # Add more species as needed
    ]

    # choices for breed (expand it...)
    BREED_CHOICES = [
        ('Labrador Retriever', 'Labrador Retriever'),
        ('German Shepherd', 'German Shepherd'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Mixed Breed', 'Mixed Breed'),
        ('Other', 'Other')
        # add more breeds
    ]

    # fields for pet record
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='U')
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=50, choices=BREED_CHOICES)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE, related_name='pets')
    pet_img = models.ImageField(null=True, blank=True, upload_to="images/")


