
# PyPetstore

PyPetstore is a very basic command-line tool written in Python that helps managing the sales process of selling pets. The application is inspired by [JPetstore](https://github.com/seokyoungkim/jpetstore6), a more extensive Java application that is often used by researchers to validate techniques that cluster software into coherent microservice boundaries. The aim of PyPetstore is similar, but then can be used for Python applications instead. This means, PyPetstore serves as a 'toy' example in which we can validate the working of [PyMonosplitter](https://github.com/larsvasseldonk/pymonosplitter). PyMonosplitter takes the source code of PyPetstore as an input, extract static, semantic and dynamic dependencies, and uses this information to define loosely coupled and highly cohesive microservice recommendations. 

## Getting started
Use the following command to run the application:

`python -m pypetstore.main`

This means that you have to run the app as a module, and not as a Python script.
