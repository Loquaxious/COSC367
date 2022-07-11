"""
Make the following CSP arc consistent by modifying the code (if necessary) and pasting the result in the answer box.

from csp import CSP
canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })

Notes and remarks

    Remember to include the import statement in your answer.
    All the example (test) cases of this question are hidden.
    This instance of CSP is also an instance of the graph colouring problem with only two colours which can be solved (or decided) in linear time. So a generic CSP algorithm is not really the best choice to solve this problem. Nevertheless, this is a good exercise.
    Before making the network arc-consistent, think whether it could have any solution. Then think what would you expect the arc-consistency outcome to be. Finally make the network arc-consistent. The end-result may surprise you!
    Think what would happen if instead of three separate constraints, we had one constraint that is the conjunction of these three; that is, christchurch != waimakariri and christchurch != selwyn and selwyn != waimakariri.
"""

from csp import CSP
canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })