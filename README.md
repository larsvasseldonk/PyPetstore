
# PyPetstore

PyPetstore is a very basic command-line tool written in Python that helps managing the sales process of selling pets. The application is inspired by JPetstore, a more extensive Java application that is often used by researchers to validate proposed techniques that cluster software into coherent microservice boundaries. The aim of PyPetstore is similar, but then can be used for Python applications instead. This means, PyPetstore serves as an 'toy' example in which we can validate the working of our proposed technique. In our technique, we take the source code of PyPetstore as an input, extract static, semantic and dynamic dependencies, and use this information to make loosely coupled and highly cohesive microservice recommendations. 

## Getting started
Use the following command to run the application:

`python -m pypetstore.main`

This means that you have to run the app as a module, and not as a Python script.
