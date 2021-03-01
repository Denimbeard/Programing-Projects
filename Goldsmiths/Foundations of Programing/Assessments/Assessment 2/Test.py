class Database(object): 
    database = []

    # Counter for student total
    studentid = 000  
    
    # Bool states for functions
    addstate = False
    restate = False
    rosstate = False
    exstate = False
    grastate = False

      def __init__ (self):
        self.first = str(input('Students Given Name: '))
        self.last = str(input('Students Surname: '))
        # self.sid = id(self)

        """ Adds new item to list called studentList """
        studentList.append(self)
        
        """ Ups counter to track how many entries """
        Database.studentid += 1

        
        print('{} {} has been added to the database.'.format(self.first, 
            self.last))
    
    def __str__(self):
        return '{} {}'.format(self.first, self.last)

    def main():
        """
        User choice starts blank
        Could it be Null? Not sure if it matters.
        """

        _user = None
        
        """ Available options, to guarantee that they have a correct one. """
        choice = ['A', 'R', 'L', 'G', 'X']
        
        """ While user input is null, offer to accept input. """
        while _user is None:
            _user = input("Choose 'A', 'R', 'L' or 'G' (‘X’ for exit): ")
            
            """ Check that the user has entered an appropriate option, otherwise offer main menu. """
            
            try:
                _user in choice 
            except:
                Database.main()      
        
        """ Once a choice is made, perform the following action and then offer main menu again. """
        if _user in choice:
            
            """ Initiates class as new instance to build a student """
            if _user == 'A':
            #    print('Adding Student')
                Database()
                Database.main()
           
            """ Will Remove a class instance """
            if _user == 'R':
                Database.remove()
                print('Removing Student') 
                Database.main()
            
            """ Will list all available instances """
            if _user == 'L':
                print('List of Students: \n')
                for obj in studentList: 
                    print( obj.first, obj.last, sep =' ' )
                Database.main()
            
            """ Will add grades to class instance (See class init for maths) """
            if _user == 'G':
                print('Student Grade')
                Database.main()
            
            """ If X is chosen, close system and do not offer main menu. """
            if _user == 'X':
                   exstate()
        else:
            Database.main()

    """ Will Remove a class instance """    
    def remove(): 
        first = input('Students first name: ')
        last = input('Students surname: ')
        
        
        

    """ Will list all available instances """
    #def roster():
    #    pass
    
    """ If X is chosen, close system and do not offer main menu. """
    def exstate():
        print('Thank You')
        print('Goodbye!')
        exit()

    """ Will add grades to class instance (See class init for maths) """
    #def grade():
    #    pass

    """ Offers Full Name"""
    def fullname(self):

studentList = []

Database.main()

def main():
        __user = None
        __choice = ['A', 'R', 'L', 'X']

        """ While user input is null, offer to accept input. """
        while _user is None:
            __user = input("Choose 'A', 'R', 'L' or 'G' (‘X’ for exit): ")
            
            """ Check that the user has entered an appropriate option, otherwise offer main menu. """
            try:
                __user in choice 
            except:
                Student.main()      
        
        """ Once a choice is made, perform the following action and then offer main menu again. """
        if __user in choice:
            
            """ Initiates class as new instance to build a student """
            if __user == 'A':
            #    print('Adding Student')
                first = str(input('Students Given Name: '))
                last = str(input('Students Surname: '))
                Student(first, last)
                Student.main()
           
            """ Will Remove a class instance """
            if __user == 'R':
                Student.remove()
                print('Removing Student') 
                Student.main()
            
            """ Will list all available instances """
            if __user == 'L':
                print('List of Students: \n')
                for obj in studentList: 
                    print( obj.first, obj.last, sep =' ' )
                Student.main()
            
            """ Will add grades to class instance (See class init for maths) """
            if __user == 'G':
                print('Student Grade')
                Student.main()
            
            """ If X is chosen, close system and do not offer main menu. """
            if __user == 'X':
                   exstate()
        else:
            Student.main()