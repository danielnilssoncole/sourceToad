# Python 2.7.11
# Given the following list/dictionary.
# Write a single function to punch out
# it's nested key value pairs at any level
# for easy display to the user.

my_list = [
{
    'guest_id': 177,
    'guest_type': 'crew',
    'first_name': 'Marco',
    'middle_name': None,
    'last_name': 'Burns',
    'gender': 'M',
    'guest_booking': [{
        'booking_number': 20008683,
        'ship_code': 'OST',
        'room_no': 'A0073',
        'start_time': 1438214400,
        'end_time': 1483142400,
        'is_checked_in': True
    }],
    'guest_account': [{
        'account_id': 20009503,
        'status_id': 2,
        'account_limit': 0,
        'allow_charges': True
    }]
},
{
    'guest_id': 10000113,
    'guest_type': 'crew',
    'first_name': 'Bob Jr ',
    'middle_name': 'Charles',
    'last_name': 'Hemingway',
    'gender': 'M',
    'guest_booking': [{
        'booking_number': 10000013,
        'room_no': 'B0092',
        'is_checked_in': True
    }],
    'guest_account': [{
        'account_id': 10000522,
        'account_limit': 300,
        'allow_charges': True
    }]
},
{
    'guest_id': 10000114,
    'guest_type': 'crew',
    'first_name': 'Al ',
    'middle_name': 'Bert',
    'last_name': 'Santiago',
    'gender': 'M',
    'guest_booking': [{
        'booking_number': 10000014,
        'room_no': 'A0018',
        'is_checked_in': True
    }],
    'guest_account': [{
        'account_id': 10000013,
        'account_limit': 300,
        'allow_charges': True
    }]
},
{
    'guest_id': 10000115,
    'guest_type': 'crew',
    'first_name': 'Red ',
    'middle_name': 'Ruby',
    'last_name': 'Flowers ',
    'gender': 'F',
    'guest_booking': [{
        'booking_number': 10000015,
        'room_no': 'A0051',
        'is_checked_in': True
    }],
    'guest_account': [{
        'account_id': 10000519,
        'account_limit': 300,
        'allow_charges': True
    }]
},
{
    'guest_id': 10000116,
    'guest_type': 'crew',
    'first_name': 'Ismael ',
    'middle_name': 'Jean-Vital',
    'last_name': 'Jammes',
    'gender': 'M',
    'guest_booking': [{
        'booking_number': 10000016,
        'room_no': 'A0023',
        'is_checked_in': True
    }],
    'guest_account': [{
        'account_id': 10000015,
        'account_limit': 300,
        'allow_charges': True
    }]
}
]


def punchOut(a_list, *args):
    #call this function with only one input. ex: punchOut(my_list) .
    #do not call the funciton with any additional arguments.
    #optional arguments are used in the recursion step of the function
    #for proper tabbing when displaying lower levels of the list of dictionaries
    if len(args) > 0 and args[0] == 1:
        tabs = '\t'
    else:
        tabs = ''
    for dict in a_list:
        nested = [i for i in dict.values() if type(i) == list]
        if len(nested) > 0:
            print('{}{}'.format('*'*75,'\n'))
        for k,v in dict.items():
            if type(v) != list:
                print('\t{}{} : {}'.format(tabs, k, v))
            else:
                print('\n\t{}'.format(k))
                punchOut(v, 1)
        print('')


if __name__ == '__main__':
    punchOut(my_list)
