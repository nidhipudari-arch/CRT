#linear search implementation
def linear_search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return i
    return -1
print(linear_search([12,45,78,69,32], 12))
print(linear_search([12,45,78,69,32], 78))
print(linear_search([12,45,78,69,32], 32))
print(linear_search([12,45,78,69,32], 200))