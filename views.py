from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm




def index(request):
    form = CustomerForm
    
    context = {'form':form}


    if request.method =='POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
            form.save()

    
    return render(request, 'personal_portfolio/templates/index.html', context)

def dicecompanionView(request):
    return render(request, 'dicecompanion.html')

def dicecompanionRules(request):
    return render(request, 'rules.html')

#These are some GLobals I experimented with
currentScore = 0
roundNumber = 0
rollsThisRound = 0

def dicecompanionIndex(request):
    global currentScore
    global roundNumber
    global rollsThisRound
    if request.method =='POST':
        form = CustomerForm
        message = 'Nice Roll!'
        
        ##HEY LOOK RIGHT HERE!!! THIS IS HOW YOU GET THE STRING FROM THE FIELD!!!!
        currentRoll = request.POST.get('enter_number')
        
        #This processes the user input
        if currentRoll == '1':
            currentScore = 0
            message = 'Reset Score!'
            roundNumber += 0
        elif currentRoll == '2':
            if currentScore != 0:
                currentScore += currentScore
            else:
                currentScore += 2

            message = 'Doubled it!'
            rollsThisRound += 1
        elif currentRoll == '3':
            currentScore += 3
            rollsThisRound += 1   
        elif currentRoll == '4':
            currentScore += 4 
            rollsThisRound += 1 
        elif currentRoll == '5':
            currentScore += 5 
            rollsThisRound += 1  
        elif currentRoll == '6':
            currentScore += 6 
            rollsThisRound += 1
        else:
            message = 'INVALID ENTRY'
            print('Invalid number')
            

        form = CustomerForm(request.POST)
        #using a list lets us post multiple things
        values = {'form': form, 'answer': currentScore, 'message': message, 'round': roundNumber, 'rolls': rollsThisRound}

        if form.is_valid():
            
            return render(request, 'index.html', values)
            
    else: #GET
        form = CustomerForm(request.POST)
        message = 'Get Ready to Play!'
        values = {'form': form, 'message': message}
        return render(request, 'index.html', values)

def add(request):
    """
    Process request to add new item to the inventory.  Return back to the 
    main index page when done.
    """
    # Read values from GET request (TODO: Add error checking here)
    try:
        item_id = 'dso'
        description = 'dddoodo'
        value = None
        hazardous = None
        return render(request, 'dicecompanion.html')

    except Exception as e:
        # TODO: Send an error message back to the main index page
        print("Unable to save to database: {}".format(e))

    # Return to main index page
    
# Create your views here.
