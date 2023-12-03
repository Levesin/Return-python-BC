offer = input("Предложение из двух слов: ")
mod_offer, mod_offer2 = offer.split()
source_file = open('test.txt', 'w')

print(offer, file=source_file, end=" <<<>>> \n")
print(mod_offer, file=source_file, end=" <<<>>> \n")
print(mod_offer2, file=source_file, end=" <<<>>> \n")

format_one = '! %s %s ?' % (mod_offer.upper()[::-1], mod_offer2.capitalize()[::-1])
print(format_one, file=source_file, end=" <<<>>> \n")

format_two = '! {0} {1} ?'.format(mod_offer.upper()[::-1], mod_offer2.capitalize()[::-1])
print(format_two, file=source_file, end=" <<<>>> \n")

format_three = f'! {mod_offer.upper()[::-1]} {mod_offer2.capitalize()[::-1]} ?'
print(format_three, file=source_file, end=" <<<>>> \n")

source_file.close()
