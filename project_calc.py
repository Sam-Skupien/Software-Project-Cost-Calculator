'''
TO-DO:
- convert from char to int on some caluclations!!!!
'''

import sys


def gui_calc():

    '''
                                    GUI Component Function
    '''
    GUI_comp = '''
    Build Component cost = cost to build + cost to maintain components you build
    Purchase Component cost = Developer cost + End user cost + maintenance cost for components you buy
    Buy a component if: Build Component cost > Purchase component cost
    Improvement in productivity factor for GUI components = 0.4
    Your application reuse savings = (0.4 x cost to build) x (number of applications - 1)
    Your cost per user = Component cost / sum of users across all applications (ignoring overlap in users)
    '''
    print()
    print()
    print('Beginning GUI Component Cost Computation.')
    print()
    print('Equation: ')
    print()
    print(GUI_comp)
    print('-----------------------------------------------------------------------')

    gui_prod_factor = 0.4
    num_apps = 50

    cost_to_build = input("Enter cost to build GUI component:    ")
    cost_to_maintain = input("Enter cost to maintain GUI component:    ")
    dev_cost = input("Enter cost to develop GUI:    ")
    end_user_cost = input("Enter end user cost:     ")
    purchased_comp_maint_cost = input("Enter purchased componenent Maintain cost:   ")
    # Build Component cost & purchase component cost
    bcc = cost_to_build + cost_to_maintain
    pcc = dev_cost + end_user_cost + purchased_comp_maint_cost
    print()
    print('Build Component Cost:    ' + bcc)
    print('Buy Component Cost:    ' + pcc)
    print('Should you build or buy this Component?')
    print()
    print('------------------')
    if bcc > pcc:
        print('Buy this component. ')
        component_cost = pcc
    else:
        print('Develop Component in-house')
        component_cost = pcc


    print('App Reuse Savings & Cost Per User')
    print()
    gui_reuse_savings = (gui_prod_factor * cost_to_build) * (num_apps -1)
    cost_per_user = component_cost / 10000
    print('App Reuse Savings:    ' + gui_reuse_savings)
    print('Cost per User:    ' + cost_per_user)
    print('End of GUI component Cost Computation')
    print('--------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------')
    print()
    print()



def serv_calc():

    '''
                                    Service Component Function
    '''
    serv_comp = '''
    Complexity cost = middleware cost + operational support cost
                          + hardware + organizational readiness cost

    Impovement in productivity factor for service components = 1.5

    Your application reuse savings = ((1.5 x cost to build) x (number of applications - 1))
                           - Complexity cost

    Your cost per user = (Component cost + Complexity cost)/ sum of users across applications
                      (ignoring overlap in users)
    '''
    print()
    print()
    print('Beginning Service Component Cost Computation.')
    print()
    print('Equation: ')
    print()
    print(serv_comp)
    print('-----------------------------------------------------------------------')
    print()

    prod_imp_factor = 1.5

    middleware_cost = input('Enter Middleware Cost:    ')
    op_supp_cost = input('Enter Operation Support Cost:    ')
    hrdw_cost = input('Enter hardware Cost:    ')
    org_read_cost = input('Enter Organizational Readiness Cost')

    serv_complexity_cost = middleware_cost + op_supp_cost + hrdw_cost + org_read_cost
    serv_reuse_savings = (prod_imp_factor * serv_complexity_cost) * (num_apps - 1) - serv_complexity_cost
    serv_cost_per_user = (component_cost + serv_complexity_cost)/10000

    print('App Reuse Savings & Cost Per User')
    print()
    print('Service Component Complexity Cost:    ' + serv_complexity_cost)
    print('Service Component Reuse Savings:    ' + serv_reuse_savings)
    print('Service Component Cost per User:    ' + serv_cost_per_user)
    print('End of Service Component Cost Computation')
    print('--------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------')
    print()
    print()


def dom_calc():

    '''
                                        Domain Component Function
    '''
    dom_comp = '''
    Domain build cost = sum of costs for the domain components and supporting
                       components + application framework costs
    Improvement in productivity factor for domain components = 10
    Your application reuse savings = ((10 x domain build cost) x (number of applications - 1))
                                      - Complexity cost
    Your cost per user = (domain build cost + complexity cost)/sum of users across all applications
                          (ignoring overlap in users)
    '''
    print()
    print()
    print('Beginning Domain Component Cost Computation.')
    print()
    print('Equation: ')
    print()
    print(dom_comp)
    print('-----------------------------------------------------------------------')
    print()

    prod_factor_dom = 10

    dom_comp_cost = input('Enter the Total Sum of costs for all Domain Components:   ')
    dom_supp_cost = input('Enter the Total Sum of costs for all Supporting Components:    ')
    app_frame_costs = input('Enter the Application Framework Costs')
    complex_cost = input('Enter the complexity cost')


    dom_build_cost = dom_comp_cost + dom_supp_cost + app_frame_costs
    dom_app_reuse_sav = ((prod_factor_dom * dom_build_cost) * (num_apps - 1)) - complex_cost
    cost_per_user = (dom_build_cost + complex_cost)/ 10000

    print('Domain Component Cost')
    print()
    print('Domain Application Build Cost:    ' + dom_build_cost)
    print('Domain Application Reuse Savings:    ' + serv_reuse_savings)
    print('Domain Application Cost per User:    ' + serv_cost_per_user)
    print('End of Domain Application Cost Computation')
    print('--------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------')
    print()
    print()

def main():
    print('Please pick one of the following modules for computation')
    print('--------------------------------------------------------')
    print('1)   GUI Component Cost')
    print('2)   Service Component Cost')
    print('3)   Domain Component Cost')
    print('4)   End Program')
    print('--------------------------------------------------------')
    uchoice = input('Enter the compution you would like to choose:    ')

    if uchoice == '1':
        gui_calc()
    elif uchoice == 2:
        serv_calc()
    elif uchoice == 3:
        dom_calc()
    elif uchoice == 4:
        sys.exit(0)
    else:
        print('Whoops, that was the wrong key! Bye!')

main()
