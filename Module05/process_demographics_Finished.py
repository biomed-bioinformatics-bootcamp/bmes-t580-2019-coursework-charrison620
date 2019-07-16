#Updated with infection length, coinfection, and on_therapy
import csv
import os

def main():

    print_the_header()
    filename = get_filename()
    age_min, age_max = get_age_cutoff()
    min_infection_length, max_infection_length = get_infection_length_cutoff()
    match_therapy_criteria = get_therapy_criteria()
    match_coinfection_criteria = coinfection()
    num_pats = 0
    pats = []

    # Open file and start reader
    with open(filename) as handle:
        reader = csv.DictReader(handle)

        for row in reader:
            pat_age = int(row['AGE'])
            infection_length = int(row['INFECTION_LENGTH'])
            on_therapy = str(row['ON_THERAPY'])
            any_coinfection = str(row['COINFECTION'])


            # Seperate out the long logic for clarity
            match_age = (pat_age > age_min) and (pat_age < age_max)
            match_infection_length = (infection_length > min_infection_length) and (infection_length < max_infection_length)


            if match_age and match_infection_length and (match_therapy_criteria == on_therapy) and (match_coinfection_criteria == any_coinfection):
                num_pats += 1
                pats.append(row)


    with open('pat_data.csv' + '.valid', 'w') as handle:
        fields = ['PAT_NUM', 'SEX', 'AGE', 'INFECTION_LENGTH', 'ON_THERAPY', 'COINFECTION']
        writer = csv.DictWriter(handle, fields, delimiter=',')
        writer.writeheader()

        for row in pats:
            writer.writerow(row)


    print('Based on the following criteria:')
    print(' - Age: [%i, %i]' % (age_min, age_max))

    print('There are %i eligible patients' % num_pats)



def print_the_header():
    print('---------------------------------')
    print('       Process Demographics')
    print('---------------------------------')
    print()


def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename

def get_age_cutoff():

    age_min, age_max = None, None
    while age_min is None:
        age_inp = input('What is the youngest age for the study? ')
        try:
            age_min = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again')
            continue

        if age_min < 18:
            print('Ethics boards require special permission for youth cohort. Please pick an older age')
            age_min = None

    while age_max is None:
        age_inp = input('What is the oldest age for the study? ')
        try:
            age_max = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again')
            continue

    return age_min, age_max

def get_infection_length_cutoff():

    min_infection_length, max_infection_length = None, None
    while min_infection_length is None:
        infection_input = input('What is the minimum length of time the patient has been infected? ')
        try:
            min_infection_length = int(infection_input)
        except ValueError:
            print(infection_input + 'is not a numner, please try again. ')
            continue

    while max_infection_length is None:
        infection_input = input('What is the minimum length of time the patient has been infected? ')
        try:
            max_infection_length = int(infection_input)
        except ValueError:
            print(infection_input + 'is not a number, please try again. ')
            continue

    return min_infection_length, max_infection_length

def get_therapy_criteria():

    on_therapy = None
    while on_therapy is None:
        therapy_input = input('is the patient on therapy? ')
        if (therapy_input != 'Yes') and (therapy_input != 'No'):
            print(therapy_input + 'is not a valid answer. please try again')
            continue
        else:
            on_therapy = therapy_input

    return on_therapy


def coinfection():

    any_coinfection = None
    while any_coinfection is None:
        coinfection_input = input('does the patient have a coinfection? ')
        if (coinfection_input != 'Yes') and (coinfection_input != 'No'):
            print(coinfection_input + 'is not a valid answer. please try again. ')
            continue
        else:
            any_coinfection = coinfection_input

    return any_coinfection


if __name__ == '__main__':
    main()