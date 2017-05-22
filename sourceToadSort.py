# Python 2.7.11
# Given the above list/dictionary again.
# Write a python function/method to sort
# the top level array elements based on
# a key regardless of what level it occurs
# with in the list/dictionary (
#  i.e. sort by last_name AND/OR sort by account_id )
#  HINT: Recursion is your friend

from sourceToadPunchOut import punchOut
from operator import itemgetter

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


def getValue(dict, sort_key):
    if sort_key in dict.keys() and type(dict[sort_key]) != list:
        return dict[sort_key]
    else:
        for key in dict.keys():
            if type(dict[key]) == list and sort_key in dict[key][0].keys():
                return getValue(dict[key][0], sort_key)


def mySort(a_list, sort_key):
    first_keys = []
    first_values = []
    sort_key_values = []
    tuples = []
    sorted_list = []

    for dict in a_list:
        first_key = dict.keys()[0]
        first_value = dict[dict.keys()[0]]
        sort_key_value = getValue(dict, sort_key)

        first_keys.append(first_key)
        first_values.append(first_value)
        sort_key_values.append(sort_key_value)

        tuples.append((first_key, first_value, sort_key_value))

    s_tuples = sorted(tuples, key=itemgetter(2))

    for tup in s_tuples:
        for dict in a_list:
            if dict[tup[0]] == tup[1]:
                sorted_list.append(dict)

    return sorted_list


#using function from first part of assessment to print nicely
def punchOut(a_list, *args):
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

#used punchOut function from 1st part of assessment to print nicely
if __name__ == '__main__':
    punchOut(mySort(my_list, 'booking_number'))
