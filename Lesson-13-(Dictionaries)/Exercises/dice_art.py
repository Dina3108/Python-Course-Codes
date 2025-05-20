import random
#below escape sequences are used to print following elements
#print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')
#● ┌ ─ ┐ │ └ ┘
"┌────────────┐"
"│            │"
"│            │"
"│            │"
"│            │"
"└────────────┘"
dice_art={1:(
"┌────────────┐",
"│            │",
"│     ●      │",
"│            │",
"│            │",
"└────────────┘"),
2:(
"┌────────────┐",
"│   ●        │",
"│            │",
"│       ●    │",
"│            │",
"└────────────┘"),
3:(
"┌────────────┐",
"│  ●         │",
"│     ●      │",
"│        ●   │",
"│            │",
"└────────────┘"),
4:(
"┌────────────┐",
"│  ●      ●  │",
"│            │",
"│  ●      ●  │",
"│            │",
"└────────────┘"),
5:(
"┌────────────┐",
"│  ●      ●  │",
"│      ●     │",
"│  ●      ●  │",
"│            │",
"└────────────┘"),
6:(
"┌────────────┐",
"│  ●      ●  │",
"│  ●      ●  │",
"│  ●      ●  │",
"│            │",
"└────────────┘")
}
dice=[]
total=0
num_of_dice=int(input('How many times you want to roll the Dice?:'))

for x in range(num_of_dice):
    dice.append(random.randint(1,6))
for x in range(6):
    for y in dice:
        print(dice_art.get(y)[x],end='')
    print()

for x in dice:
    total+=x
print(f'Sum Value pf all Dice: {total}')