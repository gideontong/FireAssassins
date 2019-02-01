import random
import sys

teams = ['Wet Supremacy', 'Liquidate the Kulaks', 'Drip or Drown', 'www.damplips.com', 'Fifty Shades of Spray', 'Wet Kavanaugh', 'Ha,,007', 'WETROBOOMIN', 'Drippy Lips', 'Teenage Mutant Ninja Squirters', 'Sheck Wetty', 'Bros Before Hose', 'Soggy Style', 'So Wet It Squirts', 'Hash Slinging Splashers', '5 3/4', 'The Squirters', 'Bubbleproof Boy Scouts', 'Drip Too Hard', 'How I Wet Your Mother', 'Wet Dreamz', 'Sprayaets Anatomy', 'Little Squirters', 'Putting Out the Flame', 'Squirt Till You Hurt', 'Too Much Fun Makes Us Squirt', 'Go In Hard, Come Out Wet', 'School Squirters', 'Your Momrs a Hose', 'Hose Your Daddy', 'Hoes Down', 'Erotic Aquatics', 'Smokinr nr Soakinr ', 'Alliance of Men Who Pee Sitting Down', 'K K Spray', 'Viagra Falls', 'Lean in my Water Cup', 'Oceanrs 5', 'Wetty or Not, Here We Come', 'Drippy on my Blicky Uh', 'Beach Bitches', 'Wet Privilege', 'NSINK', 'Splash nr Dash', 'Drippie Redd', 'Fresh Squeezed Sea-men', 'THe tHirStY GOrLs', 'Yeah Ight', 'Tunde Destroyers', 'Super Splash Bros', 'Drip Drip Suck My Dick', 'Guns Nr Hoses', 'Adult Swim', 'Water Gate', 'H2Hoes', 'T.H.Sea', 'Wet nr Wild', 'Keeping Up With The Karsplashians', 'Snoop Soggy Dog', 'Shores and Beaches', 'Brandi Love 2020', 'Wetflix and Spill', 'Jehovas Wetness']

allNames = [['Rahel Bachmann', 'Maria Hernandez', 'Josh Karasik', 'Layla Keshavarzi', 'Toni Sottile'], ['Alex Li', 'Rohil Ahuja', 'Tyler Chu', 'Akhil Gutta', 'Pranav Pomalapally'], ['Ned Jacobs', 'Oliver Wyman', 'Hirad Aboulghazemzadeh', 'Alex Whitehouse', 'Nick Norris'], ['Will Hollister', 'Peter Beer', 'Shawn Shepard', 'Jeremy Mettel', 'Garret Chen'], ['Jake Lippel', 'Sammie Schalk', 'Nate Arnold', 'Shayla Madha', 'Colin Iversen'], ['Conner Chen', 'Brett Goldman', 'Sophia Brent', 'Elliot Kim', 'Sona Bhargava'], ['Landon Stern', 'Bodie Devries', 'Eric Budnik', 'Hayden Becker', 'Dele Giwa'], ['Tristan Carta', 'Cade Kritsch', 'Cole Schiffer', 'Kasra Arjomand', 'Jason Weisenfeld'], ['Danny Hernandez', 'Kevin Taylor', 'Kevin Bleier', 'Eddie Hernandez', 'Chad McMillan'], ['Bryan Jimenez', 'Victor Cano', 'Ylse Prieto', 'Lorraine Campos', 'America Gutierrez'], ['Carson Batie', 'Bethany Reader', 'Gabi Dajic', 'Faviola Colon', 'Leyla Vahadi'], ['Grace Butler', 'Monique Savner', 'Caroline Dority', 'Gabrielle Grossman', 'Charlotte Chipembere'], ['Olivia Dubell', 'Michelle Hou', 'McKenna Katzman', 'Heather Arancon', 'Paris Hartman'], ['Allinta Tadesse', 'Maya Singh', 'Titan Teachman', 'Rylee Tilton', 'Claire Moats'], ['Julia Steinman', 'Devon Estes', 'Katie Reul', 'Sam Smart', 'Dawson Lamas'], ['Parker Clemons', 'Morgan Dye', 'Kyle Valestrino', 'Grady Johnson', 'Makena Pratt'], ['Ethan Wildermuth', 'Kyle Norvell', 'Cole Jolin', 'Corbin Stern', 'Bijan Kazemi'], ['Nina Ferrer', 'Amari Huang', 'Jamie Lee', 'Jiasen Jing', 'Julia Zhong'], ['Ronnie Tronconi', 'Josh Binsol', 'Xavier Zaldana', 'Ali Sallam', 'Elijah Taylor'], ['Ally Arnold', 'Bridgette Rosebrugh', 'Mariah Villavicencio', 'Christian Onuigbo', 'Emma Adams'], ['Julia Marek', 'Chloe Nash', 'Julian Giessinger', 'Taylor Marlowe', 'Jeffery Goodwin'], ['Jennifer Ruffing', 'Claire Robbins', 'Milla Wu', 'Ashley Webb', 'Megan King'], ['Julia Schiff', 'Bianca Rutten', 'Hailey Flatt', 'Elise Vigna', 'Bianca Nurnberger'], ['Dylan Hampton', 'Lance Minkow', 'Bryce Howard', 'Mason Thompson', 'CJ Woodall'], ['Chloe Snyders', 'Alexa Jabbour', 'Faith Johnson', 'Blake Thompson', 'Olivia Aleks'], ['Kelly Mason', 'Sydney Schlesinger', 'Natalie Nitzsche', 'Madison Melito', 'Raquel Startz'], ['Gaby Hayon', 'Jeremy Marcin', 'Jillian Gallardo', 'Melanie Zhang', 'Fiona Watkins'], ['Paul Grace', 'Makoa Dacascos', 'Justin Fealy', 'Colton Bourne', 'Ben Spiers'], ['David Fratello-Hakim', 'McCoy Eackelbary', 'Ian Guss', 'Bryce Kilkenny', 'Ethan Orlowsky'], ['Kelin Mahon', 'Gaby Plascencia', 'Baylee Heximer', 'Cameron Jasmin', 'Alex Dohn'], ['Allegra Skyy', 'Nicole Previde', 'Marina Mendoza', 'Zoe Haines', 'Maya Van Dien'], ['Sarah Upton', 'Alexa Campbell', 'Katelyn Patillo', 'Natalie Zavala', 'Tia Catalano'], ['Lily Garelick', 'Maggie Henry', 'Mina Dake', 'Layne Consales', 'Brandy Alps'], ['Scott Pugh', 'Kevin Garand', 'Ethan Harrison', 'Michael Wood', 'David Connor'], ['Marcandrew Choi', 'Eden Rosales', 'Alan Gallardo', 'Ashwin Soitkar', 'Bryan Xiao'], ['Conor Dower', 'Brett Fornatoro', 'Drake Nienow', 'Bradley Buckingham', 'Avi Kapur'], ['Ashley Freeborg', 'Isabelle Dempsey', 'Kennedy Crowley', 'Ashley Bolger', 'Hadley MacDonald'], ['Jennifer Matiz', 'Ashley Jou', 'Kayla Jou', 'Marina Bayless', 'Jada Broughton'], ['Jacob Ginzburg', 'Gideon Tong', 'Victor Bai', 'Taylor Chen', 'Anthony Haas'], ['Sonia Milio', 'Chloe Morgan', 'Valeria Barzola', 'Katelyn Waters', 'Aivy Nguyen'], ['Rucchi Dua', 'Jade Morrisey', 'Sabrina England', 'Morgan Williams', 'Josephine Martinelli'], ['Tommy Gonzalez', 'Dylan Jarvis', 'Mitchell Craig', 'Shayan Ghara', 'Preston Knapp'], ['Emiko Ito', 'Charlie Clark', 'Ian Sherril', 'Martin White', 'Zella Vacaron'], ['Will Decker', 'Hayden Vaughn', 'Ryan Downard', 'Colby Downard', 'Alexa Dickey'], ['Malia Capen', 'Diya Sinha', 'Kavyaa Thakkar', 'Blaise Liu', 'Naomie DiMartino'], ['Dylan Leong', 'Rudy Zhang', 'Monika Lopez', 'Trenton Howard', 'Cleavon Andrade'], ['Rachel Zhitnitsky', 'Mary Bissonette', 'Elizabeth Crisp', 'Isabel Galvin', 'Lorelei Lemon'], ['Sam Samalya', 'Justin Sprague', 'Erick Villegas', 'Fernando Bass', 'Carlos Higareda'], ['Mason Macdougal', 'Kade Aplin', 'Dylan Yamamoto', 'Dane Flanders', 'Tristan Becker'], ['Caelyn Pender', 'Connie Shi', 'Faiz Surani', 'Chloe Brill', 'Conner Brinkley'], ['Michael Shahidi', 'Cristian Gomez', 'Sarah Sullivan', 'Jacob Valladares', 'Olivia Dinardo'], ['Karli Lewis', 'Daisy Jones', 'Sydney Lester', 'Molly Beals', 'Amelia Brannigan'], ['Jack Gelman', 'Madison Long', 'Ethan Abes', 'Colin Ward', 'Rose Gelman'], ['Ryan Bough', 'Guillermo Castro', 'Noah Bluth', 'John Smith', 'Colby Austin'], ['Melissa De La Cruz', 'Celeste Castro', 'Rachel Mex', 'Crystal Gonzalez', 'Diana Martinez'], ['Jacqueline Gomez', 'Taylor Jones', 'Emerson Kapture', 'Sofia Kenney', 'Ethan Sherwood'], ['Clare Whitney', 'Hannah Scarborough', 'Megan Parkinson', 'Christine Collins', 'Sage Mare'], ['Kiera Price', 'Autumn Jones', 'Courtney Lam', 'Ali Karasik', 'Joey Sipos'], ['Kelby Lewis', 'Alexis Davila', 'Lexi Kerner', 'Jamee Lary', 'Cat Young'], ['Jordan Hossini', 'Sjors Lap', 'Taylor Bolger', 'Brooke Sommers', 'Ashton Valdovinos'], ['Will Lyman', 'Jason Heller', 'Chaz Meizner', 'Stone Martin', 'Terrell Vaughn'], ['Claire Adams', 'Hannah Lee', 'Victoria Nguyen', 'Josh Lunsford', 'Josseline Hernandez'], ['Aarun Devgan', 'Spencer Walshaw', 'Ryan Lam', 'Aden Fruehling', 'Connor Elstein']]

random.seed(int(sys.argv[1]))


def assignTargets(teams, allNames):
    used = []
    rList = random.sample(range(5* len(teams)), 5*len(teams))

    for i in range(5):
        if (rList[5 * len(teams) - 1 - i]/5 == len(teams) - 1):
            temp = rList[i]
            rList[i] = rList[5 * len(teams) - 1 - i]
            rList[5 * len(teams) - 1 - i] = temp
        
        passed = []
        currentIndex = 0
        passedIndex = 0

        for i in range(len(teams)):
            '''print(teams[i] + " Targets: ")'''
            
            for j in range(5):
                if (currentIndex < 5 * len(teams)):
                    rt = int(rList[currentIndex]/5)
                    rp = rList[currentIndex] % 5
                    currentIndex += 1

                    while(rt == 1):
                        passed.append(rList[currentIndex - 1])
                        rt = int(rList[currentIndex]/5)
                        rp = rList[currentIndex] % 5
                        currentIndex += 1
                    
                    used.append(allNames[rt][rp])
                    '''print(allNames[rt][rp])'''
                
                else:
                        rt = int(passed[passedIndex]/5)
                        rp = passed[passedIndex] % 5
                        passedIndex += 1
                        used.append(allNames[rt][rp])
                        '''print(allNames[rt][rp])'''
                
            """print('\n')"""
            if(teams[i] == "Wetty or Not, Here We Come"):
                """print("Checking: " + allNames[rt][rp])"""
                if(allNames[rt][rp] == "Katelyn Patillo"):
                    print("Possible seed found! " + sys.argv[1])
            
            for i in range(len(teams)):
                for j in range(5):
                    if(used.count(allNames[i][j]) != 1):
                        '''print("DO NOT USE THIS SAMPLE, RUN AGAIN")'''

assignTargets(teams, allNames)