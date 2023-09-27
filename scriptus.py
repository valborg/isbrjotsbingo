#!/usr/bin/env python3

import os
import csv
import xml.dom.minidom

import random

NUMBER_OF_CARDS = 10

# skipta upp kríteríunum í flokka:

komid = ['hefur komið til Asíu ',
 'hefur komið til suður Ameríku ',
 'hefur komið til Afríku ',
 'hefur komið til Grænlands',
 'hefur komið til Indónesíu',
 'hefur komið til Vatíkansins',
 'hefur komið til Finnlands',
 'hefur komið til Ástralíu ']
unnid = ['hefur unnið á kassa í búð ',
 'hefur unnið við matreiðslu ',
 'hefur unnið við kennslu',
 'hefur unnið á skrifstofu',
 'hefur unnið í móttöku',
 'hefur unnið á í sundlaug',
 'hefur unnið í byggingarvinnu',
 'hefur unnið við að teikna ',
 'hefur unnið sem pizzasendill',
 'hefur unnið á spítala',
 'hefur unnið í fiski',
 'hefur unnið á leikskóla']
buid = ['hefur búið á Vestfjörðum ',
 'hefur búið á Suðurlandi ',
 'hefur búið á Norðurlandi ',
 'hefur búið á Austurlandi',
 'hefur búið á Reykjarnesinu',
 'hefur búið í útlöndum']
annad = ['kann fleiri en 3 tungumál ',
 'hefur safnað frímerkjum',
 'hefur verið fremst í kóngaröð',
 'hefur farið í bingo í vinabæ',
 'var í hljómsveit ',
 'er með ofnæmi',
 'kann vel að meta tyggjóís',
 'kann að húlla með húllahring',
 'á kartöflugarð',
 'notar skó númer 45',
 'hefur fleiri en 12 lykla á lyklakippunni sinni ',
 'er með þrjár háskólagráður',
 'kann rússneska stafrófið ',
 'hefur farið í fleiri en 20 sundlaugar',
 'hefur búið til tölvuleik',
 'er með fleiri en 8 skartgripi',
 'fór í klippingu í síðustu viku ',
 'hefur keppt fyrir hönd Íslands ',
 'er með tvo bökunarofna heima hjá sér ',
 'á fleiri en 4 systkini ',
 'er einbirni',
 'á veiðistöng',
 'hefur farið oftar en einu sinni á sömu myndina í bíó ',
 'hefur dálæti á eurovision ',
 'hefur farið í sjósund',
 'á fleiri en þrjú hljóðfæri ',
 'getur farið í handahlaup ',
 'á saumavél (og kann á hana)',
 'á saumavél (og kann ekki á hana)',
 'á bókasafnskort ',
 'drekkur sjaldan kaffi',
 'vill frekar fara í bað en sturtu',
 'vill frekar fara í sturtu en bað',
 'væri til í að eiga klakavél',
 'er áskrifandi að tímariti (ekki dagblaði) ',
 'hefur farið á hestbak á þessu ári ',
 'vill frekar vaska upp í höndunum en setja í uppþvottavélina ',
 'vill frekar setja í uppþvottavélina en vaska upp í höndunum',
 'hefur farið í ikea og verslað ekkert',
 'er með mynd af börnunum sínum á ísskápnum ',
 'hefur lesið heila bók á einum degi',
 'hefur átt burkna ',
 'hefur orðið bensínlaus ',
 'hefur farið á tónleika í sundi',
 'hefur flísalagt',
 'hefur fylgist með skrefatalningunni sinni',
 'hefur dálæti af matreiðsluþáttum',
 'hefur ekki farið á skauta á tjörninni',
 'hefur farið frekar nýlega á skauta á tjörninni',
 'hefur búið til tiramisu',
 'keypti sér fjarnámskeið á netinu og kláraði það',
 'kann góða sögu um skattalöggjöf',
 'vill alltaf hafa opinn gluggann',
 'hefur séð eftir listaverkakaupum',
 'hefur haldið jólin hátíðleg á náttfötunum',
 'er með meira próf ',
 'kann uppskrift að pönnukökum utan að',
 'heitir nafni sem er fleiri en 32 stafir',
 'hefur beðið í röð til að fá að versla eitthvað ',
 'hefur byggt tréhús',
 'hefur verið í stjórn í húsfélagi ',
 'á gæludýr (hvaða dýr?) ',
 'tekur oft strætó ',
 'á smekkbuxur']

def get_card_template():
    with open(str(os.getcwd()) + "/isbrjotsbingoSnidmat.svg", "r") as f:
        return f.read()

def fill_template(template, bingo_lists):
    # hér væri hægt að setja #TITLE og #SUBTITLE
    output = template
    output = output.replace("#CRITERIA_A_1", bingo_lists[0][0])
    output = output.replace("#CRITERIA_A_2", bingo_lists[0][1])
    output = output.replace("#CRITERIA_A_3", bingo_lists[0][2])
    output = output.replace("#CRITERIA_A_4", bingo_lists[0][3])
    output = output.replace("#CRITERIA_A_5", bingo_lists[0][4])

    output = output.replace("#CRITERIA_B_1", bingo_lists[1][0])
    output = output.replace("#CRITERIA_B_2", bingo_lists[1][1])
    output = output.replace("#CRITERIA_B_3", bingo_lists[1][2])
    output = output.replace("#CRITERIA_B_4", bingo_lists[1][3])
    output = output.replace("#CRITERIA_B_5", bingo_lists[1][4])

    output = output.replace("#CRITERIA_C_1", bingo_lists[2][0])
    output = output.replace("#CRITERIA_C_2", bingo_lists[2][1])
    output = output.replace("#CRITERIA_C_3", bingo_lists[2][2])
    output = output.replace("#CRITERIA_C_4", bingo_lists[2][3])
    output = output.replace("#CRITERIA_C_5", bingo_lists[2][4])

    output = output.replace("#CRITERIA_D_1", bingo_lists[3][0])
    output = output.replace("#CRITERIA_D_2", bingo_lists[3][1])
    output = output.replace("#CRITERIA_D_3", bingo_lists[3][2])
    output = output.replace("#CRITERIA_D_4", bingo_lists[3][3])
    output = output.replace("#CRITERIA_D_5", bingo_lists[3][4])

    return output

def make_five(komid_listi, unnid_listi, buid_listi, annad_listi):
    five = []
    seed = random.random()
    if seed < 0.3:
        five.append(random.choice(komid_listi))
    seed = random.random()
    if seed < 0.45:
        five.append(random.choice(unnid_listi))
    seed = random.random()
    if seed < 0.35:
        five.append(random.choice(buid_listi))
    while(len(five) != 5):
        r = random.choice(annad_listi)
        if(r not in five):
            five.append(r)
    return five

def main():
    for i in range(NUMBER_OF_CARDS):
        card_template = get_card_template()
        bingo_lists = [make_five(komid, unnid, buid, annad), make_five(komid, unnid, buid, annad),make_five(komid, unnid, buid, annad),make_five(komid, unnid, buid, annad)]
        stuff = fill_template(card_template, bingo_lists)
        with open(f"isbrjotsbingoPrintable{i}.svg", "w") as f:
            f.write(stuff)

main()
