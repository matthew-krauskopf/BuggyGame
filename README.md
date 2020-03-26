# A BuggyGame: Security Vulnerability Midterm Project 
### Written by: Matthew Krauskopf

## Description
This python 3 application is a game where two opposing players are given identical code bases. Each player has a health bar and an amount of energy.
The opponent's health bar is visible to the player, while the amount of energy each player has is hidden. At the beginning of each turn, the player gains
1 energy, which can be increased under the improvements section. The goal of the game is to attack the opponent
and drop their health bar to 0. The game ends once one player's health reaches 0. 

## Purpose
The purpose of this project is to demonstrate how certain vulnerabilities in software systems can be exploited to the benefit of a clever attacker.
In the game, there are 4 attacks that can be executed: 1 normal attack, which can never be prevented, and 3 software exploit attacks, which can be prevented 
through code improvements. A player can gain an upperhand on their opponent by deploying these code exploit attacks. However, these attacks cost much more
energy than a standard attack, and if the target has already patched out these vulnerabilities, the energy is spent in vain. Should a player fall victim
to an attack, the damages they suffer will be costly. Repairing the fallout from the attacks will also be costly, much like the real world, so
it is in the player's interest to make sure they patch their vulnerabilities as soon as they reasonably can. 

## How to play
```
python3.6 BuggyGame.py [host|client] [port] [ip_address]
```
To start the game, one player must be the host, and one player must be the client. 

`Host|client`: simply type "host" or "client".

`Port`: pick a port number not being used by the computer currently.

`ip_address`: IP address of the person you wish to connect to.

## Explanation of attacks
### Normal Attack
#### Energy Cost: 1

This attack deals 1 damage to the opponent. Upon selecting the attack, an option will appear to enter a bonus keyword. If the word entered
matches the word found in the opponent's PrivateFiles/keyword.txt, the opponent will instead take 5 damage

### Spy Enemy Files
#### Energy Cost: 3

This attack allows the attacker to display the contents of a file located in the opponent's PublicFiles/ folder. 
This attack is vulnerable to file leakage, as files outside of PubliFiles/ can be displayed if the selected file path uses "../" to go
up a file directory. 

### Change enemy log privileges
#### Energy Cost: 5

This attack disables the write to the enemy's log file and display to their in-game log. This attack is done by removing the write permission 
on the victim's log file. Since the game can no longer write to the log file, the in-game log will display "Error! Cannot access log file. Reading privileges may have been abused"
until the issue is fixed.

### Execute DoS
#### Energy Cost: 20

This attack executes a denial of service attack on the opponent. This attack is done by sending 3 "skip" requests to the opponent in addition to the "DoS" message.
A "skip" request ends a player's turn without doing anything. This attack takes advantage of the game's request buffer system. All requests are put into a stack before 
being executed. These requests are then popped from the stack when one is to be executed. The game will prioritize popping a request from the stack over letting the player
pick their own action at the start of their turn. Since "skip" actions exist at the top of the stack, the victim of the DoS attack will be forced to skip their own turn. 
However, the attacker can still send any action they want on their turn as the game does not pop a request from the stack on the attacker's turn until 
after an action is selected. 

## Explanation of improvements
### Improve energy gain
#### Energy Cost: Variable, starts a 1

This improvement increases the amount of energy the player gains at the start of each turn. The cost of this improvement is equal
to the amount of energy gained at the beginning of that turn.

### Patch file leakage
#### Energy Cost: 5

This improvement prevents the opponent from displaying the content of any files outside of the player's PublicFiles/. This is done
by adding sanitization code before a file is read. If the requested file path contains "../", the request is rejected. 

### Patch file privileges
#### Energy Cost: 10

This improvement prevents the opponent from disabling the player's write to log files. This is done by checking the requester ID 
for the "chmod" request before executing it. If the request ID does not match the user ID, the request is rejected. 

### Patch DoS vulnerability
#### Energy Cost: 30

This improvement prevents the user from being DoS'd. This is done by limiting the number of concurrent requests from a single user to 1. If 
the opponent tries to add more than 1 request to the user's action stack, the additional requests are discarded. 


### Repair logging output
#### Energy Cost: 8

This improvement restores the functionality of the user's logging after the write permission has been removed. This is fixed by simply 
adding the write permission back to the log file.

### Reset keyword
#### Energy Cost: 10

This improvement resets the keyword that is used to determine if the opponent deals bonus damage or not in a normal attack. This is 
done by simply generating a new random keyword and overwriting the previous keyword in PrivateFiles/keyword.txt. 


## What could be improved upon
This project is essentially a Proof a Concept. It shows that a game can be developed that exploits various code vulnerabilities in a system. 
As it stands, the game is a bit shallow, with there being only a few offensive options that can be taken. Plus, the energy costs for
each action are somewhat arbitrary; there is likely an imbalance of the usefulness of some options vs their cost. A lot of play testing
would have to be done in order to properly balance all of these options. 




