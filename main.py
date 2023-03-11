
from progress.spinner import Spinner

state = 0
spinner = Spinner('Loading ')
while state != 'FINISHED':
    # Do some work
    spinner.next()


