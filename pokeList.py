import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


class pokeList:
    def __init__(self):
        pd.set_option('display.width', 1000)
        # pd.set_option('max_rows', 1000)    # Gets rid of the '...' in the rows.
        df = pd.read_csv('dataStuff/Pokemon.csv').fillna('None')

        # print(df[['Generation','Total']].mean())

        # Getting data frames for each of their respective types.
        dfWater = self.water(df)
        dfFire = self.fire(df)
        dfGrass = self.grass(df)
        dfBug = self.bug(df)
        dfDark = self.dark(df)
        dfDragon = self.dragon(df)
        dfElectric = self.electric(df)
        dfFightiing = self.fighting(df)
        dfFairy = self.fairy(df)
        dfFlying = self.flying(df)
        dfGhost = self.ghost(df)
        dfGround = self.ground(df)
        dfIce = self.ice(df)
        dfNormal = self.normal(df)
        dfPoison = self.poison(df)
        dfPsychic = self.psychic(df)
        dfRock = self.rock(df)
        dfSteel = self.steel(df)

        df_final_evos = df[df['Evolution'] == 'Final']
        # print(df_final_evos)

        # Random slices/queries here to mess around with. Easy to compare with queries like these.
        # print('Average defense of all water types: ', dfWater['Defense'].mean(), '\n')
        # print('Average defense of all fire types:  ', dfFire['Defense'].mean(), '\n')
        # print(pd.merge(dfBug, dfPoison), '\n')
        # print(df[df['Name'] == 'Blissey'], '\n')
        # print(df[df['Name'] == 'Blissey'][['HP','Defense']] * 5, '\n')
        # print(df[ (df['Type 1'] == 'Water') & (df['HP'] > 70) ], '\n')

        # df of ALL Pokemon
        df_gen_stats = self.generationStats(df)
        print('Average stats over the six generations using ALL Pokemon: \n')
        print(df_gen_stats, '\n')

        # Getting a data frame of final evolutionary stats by generation
        df_final_gen_stats = self.finalGenerationStats(df)

        print('Average stats over the six generations using only Pokemon in their FINAL EVOLUTION: \n')
        print(df_final_gen_stats, '\n')

        # For the graphing!
        self.graphing(df_final_evos)

        # self.IVCalc(df)

    # Method to show the average stats of each generation
    def generationStats(self, df):
        # print('average stats of generation 1: \n',
        #       df[df['Generation'] == 1].mean().drop(labels=['#', 'Generation', 'Legendary']), '\n')
        # print('average stats of generation 2: \n',
        #       df[df['Generation'] == 2].mean().drop(labels=['#', 'Generation', 'Legendary']), '\n')
        # print('average stats of generation 3: \n',
        #       df[df['Generation'] == 3].mean().drop(labels=['#', 'Generation', 'Legendary']), '\n')
        # print('average stats of generation 4: \n',
        #       df[df['Generation'] == 4].mean().drop(labels=['#', 'Generation', 'Legendary']), '\n')
        # print('average stats of generation 5: \n',
        #       df[df['Generation'] == 5].mean().drop(labels=['#', 'Generation', 'Legendary']), '\n')
        # print('average stats of generation 6: \n',
        #       df[df['Generation'] == 6].mean().drop(labels=['#', 'Generation', 'Legendary']), '\n')

        # The above always prints a space on the first line for each, and prints each one as a series instead of df.
        # Leaving it there as reference, though.

        df_gen_stats = pd.DataFrame()
        df_gen_stats = df_gen_stats.assign(
            Gen1=df[(df['Generation'] == 1)].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_gen_stats = df_gen_stats.assign(
            Gen2=df[(df['Generation'] == 2)].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_gen_stats = df_gen_stats.assign(
            Gen3=df[(df['Generation'] == 3)].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_gen_stats = df_gen_stats.assign(
            Gen4=df[(df['Generation'] == 4)].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_gen_stats = df_gen_stats.assign(
            Gen5=df[(df['Generation'] == 5)].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_gen_stats = df_gen_stats.assign(
            Gen6=df[(df['Generation'] == 6)].mean().drop(
                labels=['#', 'Generation', 'Legendary']))


        return df_gen_stats


    # Method that gets the stats for each generation of FINAL EVOLUTIONS of Pokemon.
    def finalGenerationStats(self, df):
        # print 'average stats of final pokemon of generation 1: \n', \
        #     df[(df['Generation'] == 1) & (df['Evolution'] == 'Final')].mean().drop(labels=['#','Generation','Legendary']), '\n'
        # print 'average stats of final pokemon of generation 2: \n', \
        #     df[(df['Generation'] == 2) & (df['Evolution'] == 'Final')].mean().drop(labels=['#','Generation','Legendary']), '\n'
        # print 'average stats of final pokemon of generation 3: \n', \
        #     df[(df['Generation'] == 3) & (df['Evolution'] == 'Final')].mean().drop(labels=['#','Generation','Legendary']), '\n'
        # print 'average stats of final pokemon of generation 4: \n', \
        #     df[(df['Generation'] == 4) & (df['Evolution'] == 'Final')].mean().drop(labels=['#','Generation','Legendary']), '\n'
        # print 'average stats of final pokemon of generation 5: \n', \
        #     df[(df['Generation'] == 5) & (df['Evolution'] == 'Final')].mean().drop(labels=['#','Generation','Legendary']), '\n'
        # print 'average stats of final pokemon of generation 6: \n', \
        #     df[(df['Generation'] == 6) & (df['Evolution'] == 'Final')].mean().drop(labels=['#','Generation','Legendary']), '\n'

        # All the above is not entirely necessary as it is taken from their resulting series and placed into a dataframe below.
        # It was mostly for visualization prior to making the dataframe.

        # df.assign() is the most efficient method to use here for adding the information extracted above as a series into a dataframe.
        df_final_gen_stats = pd.DataFrame()
        df_final_gen_stats = df_final_gen_stats.assign(
            Gen1=df[(df['Generation'] == 1) & (df['Evolution'] == 'Final')].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_final_gen_stats = df_final_gen_stats.assign(
            Gen2=df[(df['Generation'] == 2) & (df['Evolution'] == 'Final')].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_final_gen_stats = df_final_gen_stats.assign(
            Gen3=df[(df['Generation'] == 3) & (df['Evolution'] == 'Final')].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_final_gen_stats = df_final_gen_stats.assign(
            Gen4=df[(df['Generation'] == 4) & (df['Evolution'] == 'Final')].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_final_gen_stats = df_final_gen_stats.assign(
            Gen5=df[(df['Generation'] == 5) & (df['Evolution'] == 'Final')].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        df_final_gen_stats = df_final_gen_stats.assign(
            Gen6=df[(df['Generation'] == 6) & (df['Evolution'] == 'Final')].mean().drop(
                labels=['#', 'Generation', 'Legendary']))

        return df_final_gen_stats

    # Using seaborn to plot stats onto a graph to make the data easy to visualize.
    def graphing(self, df_final_evos):
        sns.set(font_scale=1.75)

        fig, ax = plt.subplots(1, 1)
        sns.stripplot(x='Generation', y='Total', data=df_final_evos, jitter=True, alpha=0.75)
        sns.barplot(x='Generation', y='Total', data=df_final_evos, color='black', alpha=0.1)
        ax.set_ylabel('Stats')

        sns.plt.show()

    # The following set of methods just return dataframes of their respective type.
    def water(self, df):
        dfWater1 = df[(df['Type 1'] == 'Water')]
        # print dfWater1, '\n'

        dfWater2 = df[(df['Type 2'] == 'Water')]
        # print dfWater2, '\n'

        dfWater = pd.merge(dfWater2, dfWater1, how='outer').fillna('None')
        dfWater = dfWater.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfWater, '\n'

        return dfWater

    def fire(self, df):
        dfFire1 = df[(df['Type 1'] == 'Fire')]

        dfFire2 = df[(df['Type 2'] == 'Fire')]

        dfFire = pd.merge(dfFire2, dfFire1, how='outer').fillna('None')
        dfFire = dfFire.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfFire, '\n'

        return dfFire

    def grass(self, df):
        dfGrass1 = df[(df['Type 1'] == 'Grass')]

        dfGrass2 = df[(df['Type 2'] == 'Grass')]

        dfGrass = pd.merge(dfGrass2, dfGrass1, how='outer').fillna('None')
        dfGrass = dfGrass.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfGrass, '\n'

        return dfGrass

    def bug(self, df):
        dfBug1 = df[(df['Type 1'] == 'Bug')]

        dfBug2 = df[(df['Type 2'] == 'Bug')]

        dfBug = pd.merge(dfBug2, dfBug1, how='outer').fillna('None')
        dfBug = dfBug.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfBug, '\n'

        return dfBug

    def dark(self, df):
        dfDark1 = df[(df['Type 1'] == 'Dark')]

        dfDark2 = df[(df['Type 2'] == 'Dark')]

        dfDark = pd.merge(dfDark2, dfDark1, how='outer').fillna('None')
        dfDark = dfDark.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfDark, '\n'

        return dfDark

    def dragon(self, df):
        dfDragon1 = df[(df['Type 1'] == 'Dragon')]

        dfDragon2 = df[(df['Type 2'] == 'Dragon')]

        dfDragon = pd.merge(dfDragon2, dfDragon1, how='outer').fillna('None')
        dfDragon = dfDragon.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfDragon, '\n'

        return dfDragon

    def electric(self, df):
        dfElectric1 = df[(df['Type 1'] == 'Electric')]

        dfElectric2 = df[(df['Type 2'] == 'Electric')]

        dfElectric = pd.merge(dfElectric2, dfElectric1, how='outer').fillna('None')
        dfElectric = dfElectric.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfElectric, '\n'

        return dfElectric

    def fighting(self, df):
        dfFighting1 = df[(df['Type 1'] == 'Fighting')]

        dfFighting2 = df[(df['Type 2'] == 'Fighting')]

        dfFighting = pd.merge(dfFighting2, dfFighting1, how='outer').fillna('None')
        dfFighting = dfFighting.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfFighting, '\n'

        return dfFighting

    def fairy(self, df):
        dfFairy1 = df[(df['Type 1'] == 'Fairy')]

        dfFairy2 = df[(df['Type 2'] == 'Fairy')]

        dfFairy = pd.merge(dfFairy2, dfFairy1, how='outer').fillna('None')
        dfFairy = dfFairy.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfFairy, '\n'

        return dfFairy

    def flying(self, df):
        dfFlying1 = df[(df['Type 1'] == 'Flying')]

        dfFlying2 = df[(df['Type 2'] == 'Flying')]

        dfFlying = pd.merge(dfFlying2, dfFlying1, how='outer').fillna('None')
        dfFlying = dfFlying.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfFlying, '\n'

        return dfFlying

    def ghost(self, df):
        dfGhost1 = df[(df['Type 1'] == 'Ghost')]

        dfGhost2 = df[(df['Type 2'] == 'Ghost')]

        dfGhost = pd.merge(dfGhost2, dfGhost1, how='outer').fillna('None')
        dfGhost = dfGhost.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfGhost, '\n'

        return dfGhost

    def ground(self, df):
        dfGround1 = df[(df['Type 1'] == 'Ground')]

        dfGround2 = df[(df['Type 2'] == 'Ground')]

        dfGround = pd.merge(dfGround2, dfGround1, how='outer').fillna('None')
        dfGround = dfGround.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfGround, '\n'

        return dfGround

    def ice(self, df):
        dfIce1 = df[(df['Type 1'] == 'Ice')]

        dfIce2 = df[(df['Type 2'] == 'Ice')]

        dfIce = pd.merge(dfIce2, dfIce1, how='outer').fillna('None')
        dfIce = dfIce.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfIce, '\n'

        return dfIce

    def normal(self, df):
        dfNormal1 = df[(df['Type 1'] == 'Normal')]

        dfNormal2 = df[(df['Type 2'] == 'Normal')]

        dfNormal = pd.merge(dfNormal2, dfNormal1, how='outer').fillna('None')
        dfNormal = dfNormal.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfNormal, '\n'

        return dfNormal

    def poison(self, df):
        dfPoison1 = df[(df['Type 1'] == 'Poison')]

        dfPoison2 = df[(df['Type 2'] == 'Poison')]

        dfPoison = pd.merge(dfPoison2, dfPoison1, how='outer').fillna('None')
        dfPoison = dfPoison.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfPoison, '\n'

        return dfPoison

    def psychic(self, df):
        dfPsychic1 = df[(df['Type 1'] == 'Psychic')]

        dfPsychic2 = df[(df['Type 2'] == 'Psychic')]

        dfPsychic = pd.merge(dfPsychic2, dfPsychic1, how='outer').fillna('None')
        dfPsychic = dfPsychic.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfPsychic, '\n'

        return dfPsychic

    def rock(self, df):
        dfRock1 = df[(df['Type 1'] == 'Rock')]

        dfRock2 = df[(df['Type 2'] == 'Rock')]

        dfRock = pd.merge(dfRock2, dfRock1, how='outer').fillna('None')
        dfRock = dfRock.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfRock, '\n'

        return dfRock

    def steel(self, df):
        dfSteel1 = df[(df['Type 1'] == 'Steel')]

        dfSteel2 = df[(df['Type 2'] == 'Steel')]

        dfSteel = pd.merge(dfSteel2, dfSteel1, how='outer').fillna('None')
        dfSteel = dfSteel.sort_values(by='#', ascending=1).reset_index(drop=True)
        # print dfSteel, '\n'

        return dfSteel

    def IVCalc(self, df):
        # IV Formula:
        # HP = ((2*Base + IV + EV/4 + 100) * Level) / 100 + 10
        # Stat = (((2*Base + IV + EV/4) * Level) / 100 + 5) * Nature
        #
        # Or when reversed:
        #
        # ((HP - 10) * 100) / Level = 2*Base + IV + EV/4 + 100
        #
        # IV = ((HP - 10) * 100) / Level - 2*Base - EV/4 - 100
        # EV = (((HP - 10) * 100) / Level - 2*Base - IV - 100) * 4
        #
        # For other stats:
        # ((Stat/Nature - 5) * 100) / Level = 2*Base + IV + EV/4
        #
        # IV = ((Stat/Nature - 5) * 100) / Level - 2*Base - EV/4
        # EV = (((Stat/Nature - 5) * 100) / Level - 2*Base - IV) * 4

        # Removed eval(input(...)) on the inputs, so if that's needed just enter it back in.

        # List of the natures, each of these has a modifier for each stat will be assigned to these natures.
        nat_list = ['Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax',
                    'Timid',
                    'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Bashful', 'Rash', 'Calm',
                    'Gentle',
                    'Sassy', 'Careful', 'Quirky']

        # Setting up a df for the modifiers of the natures.
        nat_mod = pd.DataFrame(columns=['ATK', 'DEF', 'SpA', 'SpD', 'SPE'],
                               index=nat_list)
        nat_mod['ATK'] = [1, 1.1, 1.1, 1.1, 1.1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1]
        nat_mod['DEF'] = [1, 0.9, 1, 1, 1, 1.1, 1, 1.1, 1.1, 1.1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1]
        nat_mod['SpA'] = [1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1.1, 1.1, 1.1, 1, 1.1, 1, 1, 1, 0.9, 1]
        nat_mod['SpD'] = [1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1.1, 1.1, 1.1, 1.1, 1]
        nat_mod['SPE'] = [1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1, 1.1, 1.1, 1, 1.1, 1.1, 1, 1, 0.9, 1, 1, 1, 1, 0.9, 1, 1]
        print(nat_mod, '\n')

        name = input('Enter the name of the Pokemon you want to calculate the IVs of: ').title()
        level = int(input('Enter its level: '))
        nature = input('Enter its nature: ').title()

        stat_str = input('Enter its current stats in the form of (HP / ATK / DEF / SpA / SpD / SPE): ')
        stat_arr = list(
            [_f for _f in re.split('\W+', stat_str) if _f])  # In case of there being an empty string, fastest way.
        for x in range(len(stat_arr)):
            stat_arr[x] = int(stat_arr[x])

        ev_str = input('Enter its EVs in the form of (HP / ATK / DEF / SpA / SpD / SPE): ')
        ev_arr = list(
            [_f for _f in re.split('\W+', ev_str) if _f])  # In case of there being an empty string, fastest way.
        for x in range(len(ev_arr)):
            ev_arr[x] = int(ev_arr[x])

        # hpIV = ((HP - 10) * 100) / Level - 2*Base - EV/4 - 100
        hpIV = ((stat_arr[0] - 10) * 100) / level - (2 * df[df['Name'] == name]['HP']) - ev_arr[0] / 4 - 100

        # statIV = ((Stat/Nature - 5) * 100) / Level - 2*Base - EV/4
        atkIV = ((stat_arr[1] / nat_mod.get_value(index=nature, col='ATK') - 5) * 100) / level - \
                (2 * df[df['Name'] == name]['Attack']) - ev_arr[1] / 4
        defIV = ((stat_arr[2] / nat_mod.get_value(index=nature, col='DEF') - 5) * 100) / level - \
                (2 * df[df['Name'] == name]['Defense']) - ev_arr[2] / 4
        spaIV = ((stat_arr[3] / nat_mod.get_value(index=nature, col='SpA') - 5) * 100) / level - \
                (2 * df[df['Name'] == name]['Sp. Atk']) - ev_arr[3] / 4
        spdIV = ((stat_arr[4] / nat_mod.get_value(index=nature, col='SpD') - 5) * 100) / level - \
                (2 * df[df['Name'] == name]['Sp. Def']) - ev_arr[4] / 4
        speIV = ((stat_arr[5] / nat_mod.get_value(index=nature, col='SPE') - 5) * 100) / level - \
                (2 * df[df['Name'] == name]['Speed']) - ev_arr[5] / 4

        print('IVs:')
        print(' hp: ', int(hpIV))
        print('atk: ', int(atkIV))
        print('def: ', int(defIV))
        print('spa: ', int(spaIV))
        print('spd: ', int(spdIV))
        print('spe: ', int(speIV))


pokeList()
