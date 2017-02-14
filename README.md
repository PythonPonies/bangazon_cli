# Bangazon Command Line Interface

This is a continuation of the work started here: https://github.com/PythonPonies/bangazon-api. The CLI provides a minimalistic platform from which users can create accounts, associate payment types, create orders, add products to orders, and make purchases in interaction with the Bangazon database. 

##How to Use the CLI
1. If you don't have Python version 2.7, 3.2, 3.3, 3.4, or 3.5: install the latest version of Python.

2. Clone this repository to a folder on your computer.

3. From the root folder of this repository, run `python main.py` in order to create the `bangazon.db` sqlite3 file.

4. Also from the root folder, run `python bangazon.py menu` to enter the CLI "shell". 

  1. *Important to Note*: This is not an actual shell. It functions on the basis of `sysargs` so you will need to run `python bangazon.py` and the appropriate number for the command you'd like to run. For example, if you want to create a user, then you would run `python bangazon.py 1` to see that interface. If you already have an account and would like to select it, then you would run `python bangazon.py 2`.
  
5. On each page, you will respond to the prompts in order to move along the interface and create orders, add products, and complete purchases. Wherever there is a menu showing, you will need to remember to run `pythob bangazon.py --` where the -- is the number of the menu item you'd like to navigate to.

6. Entering any command other than `python bangazon.py [1-7] or menu` will return you to the main menu. Ex: `python bangazon.py 9` or `python bangazon.py home` will return you to the main menu.

##Contributors
- [Nathan T. Baker](https://github.com/nathantbaker)
- [Steven Holmes](https://github.com/stevenwally)
- [Zoe LeBlanc](https://github.com/ZoeLeBlanc)
- [Ike Nwaelele](https://github.com/consumerike)
- [LaDonna Sales](https://github.com/sales-ls21)

