PALLET_WIDTH = 108
PALLET_LENGTH = 88
PALLET_WIDTH_PAD = 24
PALLET_LENGTH_PAD = 60
AISLE_GAP = 420

areaLength = input("Enter LENGTH of cargo area: ")

areaWidth = input("Enter WIDTH of cargo area: ")

palletDirection = input("Enter pallet side to face North/South: (Length(88\") or Width(108\")) ")

while palletDirection.casefold() not in {'width', 'length'}:
    print("You must choose Width side or Length side")
    palletDirection = input("Enter pallet side to face North/South: (Length (88\") or Width (108\")) ")

top = input("Is the Top side open? (Y/N) ")
bottom = input("Is the Bottom side open? (Y/N) ")
left = input("Is the Left side open? (Y/N) ")
right = input("Is the Right side open? (Y/N) ")

if left.casefold() == 'n' and right.casefold() == 'n' and top.casefold() == 'n' and bottom.casefold() == 'n':
    print("All sides can't be closed off!")
    exit(1)

i = 1
length = int(areaLength)
width = int(areaWidth)

palletWideNumber = 0
palletLongNumber = 0


match palletDirection.casefold():
    case 'width':
        #Calculate pallets per area width
        if left.casefold() == 'y' and right.casefold() == 'y':
            palletWideNumber = width // (PALLET_WIDTH + PALLET_WIDTH_PAD)
            if width - (palletWideNumber * (PALLET_WIDTH_PAD + PALLET_WIDTH)) > PALLET_WIDTH: palletWideNumber += 1    
        elif left.casefold() == 'y' or right.casefold() == 'y':
            palletWideNumber = width // (PALLET_WIDTH + PALLET_WIDTH_PAD)
            if width - (palletWideNumber * (PALLET_WIDTH_PAD + PALLET_WIDTH)) < PALLET_WIDTH_PAD: palletWideNumber -= 1       
        else: #TOP or BOTTOM would have to be open. So needs room for AISLE_GAP. Basically subtract 3 pallets.
            palletWideNumber = (width // (PALLET_WIDTH_PAD + PALLET_WIDTH)) - 3

        #Calculate pallets per area length
        if top.casefold() == 'y' and bottom.casefold() == 'y':
            palletLongNumber = (length // (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP)) * 2
            if length - ((palletLongNumber / 2) * (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP)) > (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH): palletLongNumber += 2
            elif length - ((palletLongNumber / 2) * (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP)) > (PALLET_LENGTH): palletLongNumber += 1
        elif top.casefold() == 'n' and bottom.casefold() == 'n':
            palletLongNumber = (length // (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) * 2
            if length - ((palletLongNumber / 2) * (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) <  PALLET_LENGTH_PAD: palletLongNumber -= 1
            elif length - ((palletLongNumber / 2) * (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) > (PALLET_LENGTH_PAD + PALLET_LENGTH + PALLET_LENGTH_PAD ): palletLongNumber += 1
        else:
            palletLongNumber = (length // (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) * 2
            if length - ((palletLongNumber / 2) * (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) > (PALLET_LENGTH_PAD + PALLET_LENGTH): palletLongNumber += 1



        
    case 'length':
        #Calculate pallets per area width
        if left.casefold() == 'y' and right.casefold() == 'y':
            palletWideNumber = (width // (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP)) * 2
            if width - ((palletWideNumber / 2) * (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP)) > (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH): palletWideNumber += 2
            elif width - ((palletWideNumber / 2) * (PALLET_LENGTH + PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP)) > (PALLET_LENGTH): palletWideNumber += 1
        elif left.casefold() == 'n' and right.casefold() == 'n':
            palletWideNumber = (width // (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) * 2
            if width - ((palletWideNumber / 2) * (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) <  PALLET_LENGTH_PAD: palletWideNumber -= 1
            elif width - ((palletWideNumber / 2) * (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) > (PALLET_LENGTH_PAD + PALLET_LENGTH + PALLET_LENGTH_PAD ): palletWideNumber += 1
        else:
            palletWideNumber = (width // (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) * 2
            if width - ((palletWideNumber / 2) * (PALLET_LENGTH_PAD + PALLET_LENGTH + AISLE_GAP + PALLET_LENGTH)) > (PALLET_LENGTH_PAD + PALLET_LENGTH): palletWideNumber += 1

        #Calculate pallets per area length
        if top.casefold() == 'y' and top.casefold() == 'y':
            palletLongNumber = length // (PALLET_WIDTH + PALLET_WIDTH_PAD)
            if length - (palletLongNumber * (PALLET_WIDTH_PAD + PALLET_WIDTH)) > PALLET_WIDTH: palletLongNumber += 1 
        elif top.casefold() == 'y' or top.casefold() == 'y':
            palletLongNumber = length // (PALLET_WIDTH + PALLET_WIDTH_PAD)
            if length - (palletLongNumber * (PALLET_WIDTH_PAD + PALLET_WIDTH)) < PALLET_WIDTH_PAD: palletLongNumber -= 1       
        else:
            palletLongNumber = (length // (PALLET_WIDTH_PAD + PALLET_WIDTH)) - 3

totalPallets = (palletWideNumber*palletLongNumber)
if totalPallets < 0: totalPallets = 0

print("Pallets are aligned by %s facing Top/Bottom." % (palletDirection))
print("Total pallets wide: %d" % (palletWideNumber))
print("Total pallets Long: %d" % (palletLongNumber))
print("-------------------")
print("Total pallets in %s by %s area: %d" % (areaLength, areaWidth, totalPallets))     