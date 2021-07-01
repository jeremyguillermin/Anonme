from simple_term_menu import TerminalMenu
from fake_useragent import UserAgent
from termcolor import colored
import subprocess
import requests
import json
import os


def MainMenu():
    subprocess.call(['clear'])
    print(colored(Main_Menu_Banner, 'magenta'))
    print(colored('1. Check your IP ', 'yellow'))
    print(colored('2. Start all in Tor', 'yellow'))
    print(colored('3. Back to the Clearnet', 'yellow'))
    print(colored('4. Chose your Tor Configuration', 'yellow'))
    print(colored('5. Use Clearnet and Search .Onion link', 'yellow'))
    print(colored('6. Information about your relay (press q to quit)', 'yellow'))
    print(colored('7. Quit\n', 'yellow'))
    
    
    while True:
        try:
            
            selection = int(input("Enter Choice : "))
            
            if selection == 1:
                Check_IP()
                break
            
            elif selection == 2:
                Start_Tor()
                break
            elif selection == 3:
                Stop_Tor()
                break

            elif selection == 4:
                Torrc_Configuration()
                break

            elif selection == 5:
                Search_Onion()
                break
            
            elif selection == 6:
                Relay_Information()
                break
            
            elif selection == 7:
                Quit()
                break

            else:
                print(colored('\nInvalide choise. Enter 1-7', 'red'))
                MainMenu()
        
        except ValueError:
            print(colored('\nInvalide choise. Enter 1-7', 'red'))
    exit


def Start_Tor():
    subprocess.call(['clear'], shell=True)
    print(colored(Start_Tor_Banner, 'magenta'))
    print(colored('\n[+] Checking TOR... ', 'green' ))
    subprocess.call(['./bash_cmd/Test_Tor.sh'], shell=True)
    subprocess.call(['./bash_cmd/Start_Tor.sh'], shell=True)
    print(colored('\n[+] Tor Service is On ...', 'green'))
    print(colored('\n[+] Checking TOR... ', 'green' ))
    subprocess.call(['./bash_cmd/Test_Tor.sh'], shell=True)
    print('\r\n')
    anykay = input(colored("Enter anything to return to main menu : ", 'yellow'))
    MainMenu()


def Stop_Tor():
    subprocess.call(['clear'], shell=True)
    print(colored(Stop_Tor_Banner, 'magenta'))
    print(colored('\n[+] Checking TOR... ', 'green' ))
    subprocess.call(['./bash_cmd/Test_Tor.sh'], shell=True)
    subprocess.call(['./bash_cmd/Stop_Tor.sh'], shell=True)
    print(colored('\n[+] Tor service is OFF ...', 'green'))
    print(colored('\n[+] Checking TOR... ', 'green' ))
    subprocess.call(['./bash_cmd/Test_Tor.sh'], shell=True)
    print('\r\n')
    anykay = input(colored("Enter anything to return to main menu : ", 'yellow'))
    subprocess.call(['clear'], shell=True)
    MainMenu()


def Torrc_Configuration():
    def Entry_Exit_Exclude():
        subprocess.call(['clear'], shell=True)
        print(colored(Entry_Nodes_Banner, 'magenta'))
        print(colored('1. Chose your Entry Nodes', 'yellow'))
        print(colored('2. Chose your Exit Nodes', 'yellow'))
        print(colored('3. Chose your Exclude Nodes', 'yellow'))
        print(colored('4. Activate your Configuration ', 'yellow'))
        print(colored('5. Delete your Configuration', 'yellow'))
        print(colored('6. Back to menu\n', 'yellow'))

        while True:
            try:
                
                selection = int(input("Enter Choice : "))
                
                if selection == 1:
                    Entry_Nodes()
                    break

                elif selection == 2:
                    Exit_Nodes()
                    break

                elif selection == 3:
                    Exclude_Nodes()
                    break

                elif selection == 4:
                    Start_Torrc_Config()
                    break

                elif selection == 5:
                    Remove_Torrc_Config()

                elif selection == 6:
                    MainMenu()

                else:
                    print(colored('\nInvalide choise. Enter 1-6', 'red'))
                    Entry_Exit_Exclude()
            
            except ValueError:
                print(colored('\nInvalide choise. Enter 1-6', 'red'))
        exit

    
    def Entry_Nodes():
            terminal_menu = TerminalMenu(
                [
        "ASCENSION ISLAND : {ac}", "AFGHANISTAN : {af}", "ALAND : {ax}", "ALBANIA : {al}", "ALGERIA : {dz}", "ANDORRA : {ad}", "ANGOLA : {ao}", "ANGUILLA : {ai}", "ANTARCTICA : {aq}", "ANTIGUA AND BARBUDA : {ag}", "ARGENTINA REPUBLIC : {ar}", "ARMENIA : {am}", "ARUBA : {aw}", "AUSTRALIA : {au}", "AUSTRIA : {at}", "AZERBAIJAN : {az}",
        "BAHAMAS : {bs}", "BAHRAIN : {bh}", "BANGLADESH : {bd}", "BARBADOS : {bb}", "BELARUS : {by}", "BELGIUM : {be}", "BELIZE : {bz}", "BENIN : {bj}", "BERMUDA : {bm}", "BHUTAN : {bt}", "BOLIVIA : {bo}", "BOSNIA AND HERZEGOVINA : {ba}", "BOTSWANA : {bw}", "BOUVET ISLAND : {bv}", "BRAZIL : {br}", "BRITISH INDIAN OCEAN TERR : {io}", "BRITISH VIRGIN ISLANDS : {vg}", "BRUNEI DARUSSALAM : {bn}", "BULGARIA : {bg}", "BURKINA FASO : {bf}", "BURUNDI : {bi}",         
        "CAMBODIA : {kh}", "CAMEROON : {cm}", "CANADA : {ca}", "CAPE VERDE : {cv}", "CAYMAN ISLANDS : {ky}", "CENTRAL AFRICAN REPUBLIC : {cf}", "CHAD : {td}", "CHILE : {cl}", "PEOPLE'S REPUBLIC OF CHINA : {cn}", "CHRISTMAS ISLANDS : {cx}", "COCOS ISLANDS : {cc}", "COLOMBIA : {co}", "COMORAS : {km}", "CONGO : {cg}", "CONGO (DEMOCRATIC REPUBLIC) : {cd}", "COOK ISLANDS : {ck}", "COSTA RICA : {cr}", "COTE D IVOIRE : {ci}", "CROATIA : {hr}", "CUBA : {cu}", "CYPRUS : {cy}", "CZECH REPUBLIC : {cz}",             
        "DENMARK : {dk}", "DJIBOUTI : {dj}", "DOMINICA : {dm}", "DOMINICAN REPUBLIC : {do}",
        "EAST TIMOR : {tp}", "ECUADOR : {ec}", "EGYPT : {eg}", "EL SALVADOR : {sv}", "EQUATORIAL GUINEA : {gq}", "ESTONIA : {ee}", "ETHIOPIA : {et}",
        "FALKLAND ISLANDS : {fk}", "FAROE ISLANDS : {fo}", "FIJI : {fj}", "FINLAND : {fi}", "FRANCE : {fr}", "FRANCE METROPOLITAN : {fx}", "FRENCH GUIANA : {gf}", "FRENCH POLYNESIA : {pf}", "FRENCH SOUTHERN TERRITORIES : {tf}",         
        "GABON : {ga}", "GAMBIA : {gm}", "GEORGIA : {ge}", "GERMANY : {de}", "GHANA : {gh}", "GIBRALTER : {gi}", "GREECE : {gr}", "GREENLAND : {gl}", "GRENADA : {gd}", "GUADELOUPE : {gp}", "GUAM : {gu}", "GUATEMALA : {gt}", "GUINEA : {gn}", "GUINEA-BISSAU : {gw}", "GUYANA : {gy}",
        "HAITI : {ht}", "MCDONALD ISLAND : {hm}", "HONDURAS : {hn}", "HONG KONG : {hk}", "HUNGARY : {hu}",
        "ICELAND : {is}", "INDIA : {in}", "INDONESIA : {id}", "ISLAMIC REPUBLIC OF IRAN : {ir}", "IRAQ : {iq}", "IRELAND : {ie}", "ISLE OF MAN : {im}", "ISRAEL : {il}", "ITALY : {it}",      
        "JAMAICA : {jm}", "JAPAN : {jp}", "JORDAN : {jo}",
        "KAZAKHSTAN : {kz}", "KENYA : {ke}", "KIRIBATI : {ki}", "DEM PEOPLES REP OF KOREA : {kp}", "REPUBLIC OF KOREA : {kr}", "KUWAIT : {kw}", "KYRGYZSTAN : {kg}",     
        "LAO PEOPLE'S DEM. REPUBLIC : {la}", "LATVIA : {lv}", "LEBANON : {lb}", "LESOTHO : {ls}", "LIBERIA : {lr}", "LIBYAN ARAB JAMAHIRIYA : {ly}", "LIECHTENSTEIN : {li}", "LITHUANIA : {lt}", "LUXEMBOURG : {lu}",
        "MACAO : {mo}", "MACEDONIA : {mk}", "MADAGASCAR : {mg}", "MALAWI : {mw}", "MALAYSIA : {my}", "MALDIVES : {mv}", "MALI : {ml}", "MALTA : {mt}", "MARSHALL ISLANDS : {mh}", "MARTINIQUE : {mq}", "MAURITANIA : {mr}", "MAURITIUS : {mu}", "MAYOTTE : {yt}", "MEXICO : {mx}", "MICRONESIA : {fm}", "REPUBLIC OF MOLDAVA : {md}", "MONACO : {mc}", "MONGOLIA : {mn}", "MONTENEGRO : {me}", "MONTSERRAT : {ms}", "MOROCCO : {ma}", "MOZAMBIQUE : {mz}", "MYANMAR : {mm}",
        "NAMIBIA : {na}", "NAURU : {nr}", "NEPAL : {np}", "NETHERLANDS ANTILLES : {an}", "THE NETHERLANDS : {nl}", "NEW CALEDONIA : {nc}", "NEW ZEALAND : {nz}", "NICARAGUA : {ni}", "NIGER : {ne}", "NIGERIA : {ng}", "NIUE : {nu}", "NORFOLK ISLAND : {nf}", "NORTHERN MARIANA ISLANDS : {mp}", "NORWAY : {no}",         
        "OMAN : {om}",
        "PAKISTAN : {pk}", "PALAU : {pw}", "PALESTINE : {ps}", "PANAMA : {pa}", "PAPUA NEW GUINEA : {pg}", "PARAGUAY : {py}", "PERU : {pe}", "REPUBLIC OF THE PHILIPPINES : {ph}", "PITCAIRN : {pn}", "POLAND : {pl}", "PORTUGAL : {pt}", "PUERTO RICO : {pr}",  
        "QATAR : {qa}",
        "REUNION : {re}", "ROMANIA : {ro}", "RUSSIAN FEDERATION : {ru}", "RWANDA : {rw}",
        "SAMOA : {ws}", "SAN MARINO : {sm}", "SAO TOME/PRINCIPE : {st}", "SAUDI ARABIA : {sa}", "SCOTLAND : {uk}", "SENEGAL : {sn}", "SERBIA : {rs}", "SEYCHELLES : {sc}", "SIERRA LEONE : {sl}", "SINGAPORE : {sg}", "SLOVAKIA : {sk}", "SLOVENIA : {si}", "SOLOMON ISLANDS : {sb}", "SOMALIA : {so}", "SOMOA,GILBERT,ELLICE ISLANDS : {as}", "SOUTH AFRICA : {za}", "SOUTH GEORGIA, SOUTH SANDWICH ISLANDS : {gs}", "SOVIET UNION : {su}", "SPAIN : {es}", "SRI LANKA : {lk}", "ST HELENA : {sh}", "ST KITTS AND NEVIS : {kn}", "ST LUCIA : {lc}", "ST PIERRE AND MIQUELON : {pm}", "ST VINCENT THE GRENADINES : {vc}", "SUDAN : {sd}", "SURINAME : {sr}", "SVALBARD AND JAN MAYEN : {sj}", "SWAZILAND : {sz}", "SWEDEN : {se}", "SWITZERLAND : {ch}", "SYRIAN ARAB REPUBLIC : {sy}",
        "TAIWAN : {tw}", "TAJIKISTAN : {tj}", "UNITED REPUBLIC OF TANZANIA : {tz}", "THAILAND : {th}", "TOGO : {tg}", "TOKELAU : {tk}", "TONGA : {to}", "TRINIDAD AND TOBAGO : {tt}", "TUNISIA : {tn}", "TURKEY : {tr}", "TURKMENISTAN : {tm}", "TURKS AND CALCOS ISLANDS : {tc}", "TUVALU : {tv}",            
        "UGANDA : {ug}", "UKRAINE : {ua}", "UNITED ARAB EMIRATES : {ae}", "UNITED KINGDOM (no new registrations) : {gb}", "UNITED KINGDOM : {uk}", "UNITED STATES : {us}", "UNITED STATES MINOR : {um}", "URUGUAY : {uy}", "UZBEKISTAN : {uz}",
        "VANUATU : {vu}", "VATICAN CITY STATE : {va}", "VENEZUELA : {ve}", "VIET NAM : {vn}", "VIRGIN ISLANDS (USA) : {vi}", 
        "WALLIS AND FUTUNA ISLANDS : {wf}", "WESTERN SAHARA : {eh}",            
        "YEMEN : {ye}",
        "ZAMBIA : {zm}", "ZIMBABWE : {zw}"
                ], multi_select=True, show_multi_select_hint=True,)
            
            menu_entry_indices = terminal_menu.show()
            print(colored('\nYour Entry Nodes Configuration : \n', 'magenta'))
            print(terminal_menu.chosen_menu_entries)
            fichier = open("data/torrc.config", "a")
            fichier.write(str(('\nEntryNodes ' + ",".join([item.split(" : ")[1] for item in terminal_menu.chosen_menu_entries]))))
            fichier.write(' StrictNodes 1')
            fichier.close()
            anykay = input(colored("\nEnter anything to return to configuration menu : ", 'yellow'))
            Entry_Exit_Exclude()        

    
    def Exit_Nodes():
            terminal_menu = TerminalMenu(
                [
        "ASCENSION ISLAND : {ac}", "AFGHANISTAN : {af}", "ALAND : {ax}", "ALBANIA : {al}", "ALGERIA : {dz}", "ANDORRA : {ad}", "ANGOLA : {ao}", "ANGUILLA : {ai}", "ANTARCTICA : {aq}", "ANTIGUA AND BARBUDA : {ag}", "ARGENTINA REPUBLIC : {ar}", "ARMENIA : {am}", "ARUBA : {aw}", "AUSTRALIA : {au}", "AUSTRIA : {at}", "AZERBAIJAN : {az}",
        "BAHAMAS : {bs}", "BAHRAIN : {bh}", "BANGLADESH : {bd}", "BARBADOS : {bb}", "BELARUS : {by}", "BELGIUM : {be}", "BELIZE : {bz}", "BENIN : {bj}", "BERMUDA : {bm}", "BHUTAN : {bt}", "BOLIVIA : {bo}", "BOSNIA AND HERZEGOVINA : {ba}", "BOTSWANA : {bw}", "BOUVET ISLAND : {bv}", "BRAZIL : {br}", "BRITISH INDIAN OCEAN TERR : {io}", "BRITISH VIRGIN ISLANDS : {vg}", "BRUNEI DARUSSALAM : {bn}", "BULGARIA : {bg}", "BURKINA FASO : {bf}", "BURUNDI : {bi}",         
        "CAMBODIA : {kh}", "CAMEROON : {cm}", "CANADA : {ca}", "CAPE VERDE : {cv}", "CAYMAN ISLANDS : {ky}", "CENTRAL AFRICAN REPUBLIC : {cf}", "CHAD : {td}", "CHILE : {cl}", "PEOPLE'S REPUBLIC OF CHINA : {cn}", "CHRISTMAS ISLANDS : {cx}", "COCOS ISLANDS : {cc}", "COLOMBIA : {co}", "COMORAS : {km}", "CONGO : {cg}", "CONGO (DEMOCRATIC REPUBLIC) : {cd}", "COOK ISLANDS : {ck}", "COSTA RICA : {cr}", "COTE D IVOIRE : {ci}", "CROATIA : {hr}", "CUBA : {cu}", "CYPRUS : {cy}", "CZECH REPUBLIC : {cz}",             
        "DENMARK : {dk}", "DJIBOUTI : {dj}", "DOMINICA : {dm}", "DOMINICAN REPUBLIC : {do}",
        "EAST TIMOR : {tp}", "ECUADOR : {ec}", "EGYPT : {eg}", "EL SALVADOR : {sv}", "EQUATORIAL GUINEA : {gq}", "ESTONIA : {ee}", "ETHIOPIA : {et}",
        "FALKLAND ISLANDS : {fk}", "FAROE ISLANDS : {fo}", "FIJI : {fj}", "FINLAND : {fi}", "FRANCE : {fr}", "FRANCE METROPOLITAN : {fx}", "FRENCH GUIANA : {gf}", "FRENCH POLYNESIA : {pf}", "FRENCH SOUTHERN TERRITORIES : {tf}",         
        "GABON : {ga}", "GAMBIA : {gm}", "GEORGIA : {ge}", "GERMANY : {de}", "GHANA : {gh}", "GIBRALTER : {gi}", "GREECE : {gr}", "GREENLAND : {gl}", "GRENADA : {gd}", "GUADELOUPE : {gp}", "GUAM : {gu}", "GUATEMALA : {gt}", "GUINEA : {gn}", "GUINEA-BISSAU : {gw}", "GUYANA : {gy}",
        "HAITI : {ht}", "MCDONALD ISLAND : {hm}", "HONDURAS : {hn}", "HONG KONG : {hk}", "HUNGARY : {hu}",
        "ICELAND : {is}", "INDIA : {in}", "INDONESIA : {id}", "ISLAMIC REPUBLIC OF IRAN : {ir}", "IRAQ : {iq}", "IRELAND : {ie}", "ISLE OF MAN : {im}", "ISRAEL : {il}", "ITALY : {it}",      
        "JAMAICA : {jm}", "JAPAN : {jp}", "JORDAN : {jo}",
        "KAZAKHSTAN : {kz}", "KENYA : {ke}", "KIRIBATI : {ki}", "DEM PEOPLES REP OF KOREA : {kp}", "REPUBLIC OF KOREA : {kr}", "KUWAIT : {kw}", "KYRGYZSTAN : {kg}",     
        "LAO PEOPLE'S DEM. REPUBLIC : {la}", "LATVIA : {lv}", "LEBANON : {lb}", "LESOTHO : {ls}", "LIBERIA : {lr}", "LIBYAN ARAB JAMAHIRIYA : {ly}", "LIECHTENSTEIN : {li}", "LITHUANIA : {lt}", "LUXEMBOURG : {lu}",
        "MACAO : {mo}", "MACEDONIA : {mk}", "MADAGASCAR : {mg}", "MALAWI : {mw}", "MALAYSIA : {my}", "MALDIVES : {mv}", "MALI : {ml}", "MALTA : {mt}", "MARSHALL ISLANDS : {mh}", "MARTINIQUE : {mq}", "MAURITANIA : {mr}", "MAURITIUS : {mu}", "MAYOTTE : {yt}", "MEXICO : {mx}", "MICRONESIA : {fm}", "REPUBLIC OF MOLDAVA : {md}", "MONACO : {mc}", "MONGOLIA : {mn}", "MONTENEGRO : {me}", "MONTSERRAT : {ms}", "MOROCCO : {ma}", "MOZAMBIQUE : {mz}", "MYANMAR : {mm}",
        "NAMIBIA : {na}", "NAURU : {nr}", "NEPAL : {np}", "NETHERLANDS ANTILLES : {an}", "THE NETHERLANDS : {nl}", "NEW CALEDONIA : {nc}", "NEW ZEALAND : {nz}", "NICARAGUA : {ni}", "NIGER : {ne}", "NIGERIA : {ng}", "NIUE : {nu}", "NORFOLK ISLAND : {nf}", "NORTHERN MARIANA ISLANDS : {mp}", "NORWAY : {no}",         
        "OMAN : {om}",
        "PAKISTAN : {pk}", "PALAU : {pw}", "PALESTINE : {ps}", "PANAMA : {pa}", "PAPUA NEW GUINEA : {pg}", "PARAGUAY : {py}", "PERU : {pe}", "REPUBLIC OF THE PHILIPPINES : {ph}", "PITCAIRN : {pn}", "POLAND : {pl}", "PORTUGAL : {pt}", "PUERTO RICO : {pr}",  
        "QATAR : {qa}",
        "REUNION : {re}", "ROMANIA : {ro}", "RUSSIAN FEDERATION : {ru}", "RWANDA : {rw}",
        "SAMOA : {ws}", "SAN MARINO : {sm}", "SAO TOME/PRINCIPE : {st}", "SAUDI ARABIA : {sa}", "SCOTLAND : {uk}", "SENEGAL : {sn}", "SERBIA : {rs}", "SEYCHELLES : {sc}", "SIERRA LEONE : {sl}", "SINGAPORE : {sg}", "SLOVAKIA : {sk}", "SLOVENIA : {si}", "SOLOMON ISLANDS : {sb}", "SOMALIA : {so}", "SOMOA,GILBERT,ELLICE ISLANDS : {as}", "SOUTH AFRICA : {za}", "SOUTH GEORGIA, SOUTH SANDWICH ISLANDS : {gs}", "SOVIET UNION : {su}", "SPAIN : {es}", "SRI LANKA : {lk}", "ST HELENA : {sh}", "ST KITTS AND NEVIS : {kn}", "ST LUCIA : {lc}", "ST PIERRE AND MIQUELON : {pm}", "ST VINCENT THE GRENADINES : {vc}", "SUDAN : {sd}", "SURINAME : {sr}", "SVALBARD AND JAN MAYEN : {sj}", "SWAZILAND : {sz}", "SWEDEN : {se}", "SWITZERLAND : {ch}", "SYRIAN ARAB REPUBLIC : {sy}",
        "TAIWAN : {tw}", "TAJIKISTAN : {tj}", "UNITED REPUBLIC OF TANZANIA : {tz}", "THAILAND : {th}", "TOGO : {tg}", "TOKELAU : {tk}", "TONGA : {to}", "TRINIDAD AND TOBAGO : {tt}", "TUNISIA : {tn}", "TURKEY : {tr}", "TURKMENISTAN : {tm}", "TURKS AND CALCOS ISLANDS : {tc}", "TUVALU : {tv}",            
        "UGANDA : {ug}", "UKRAINE : {ua}", "UNITED ARAB EMIRATES : {ae}", "UNITED KINGDOM (no new registrations) : {gb}", "UNITED KINGDOM : {uk}", "UNITED STATES : {us}", "UNITED STATES MINOR : {um}", "URUGUAY : {uy}", "UZBEKISTAN : {uz}",
        "VANUATU : {vu}", "VATICAN CITY STATE : {va}", "VENEZUELA : {ve}", "VIET NAM : {vn}", "VIRGIN ISLANDS (USA) : {vi}", 
        "WALLIS AND FUTUNA ISLANDS : {wf}", "WESTERN SAHARA : {eh}",            
        "YEMEN : {ye}",
        "ZAMBIA : {zm}", "ZIMBABWE : {zw}"
                ], multi_select=True, show_multi_select_hint=True,)
            
            menu_entry_indices = terminal_menu.show()
            print(colored('\nYour Exit Nodes Configuration : \n', 'magenta'))
            print(terminal_menu.chosen_menu_entries)
            fichier = open("data/torrc.config", "a")
            fichier.write(str(('\nExitNodes ' + ",".join([item.split(" : ")[1] for item in terminal_menu.chosen_menu_entries]))))
            fichier.write(' StrictNodes 1')
            fichier.close()  
            anykay = input(colored("\nEnter anything to return to configuration menu : ", 'yellow'))
            Entry_Exit_Exclude()

    
    def Exclude_Nodes():
            terminal_menu = TerminalMenu(
                [
        "ASCENSION ISLAND : {ac}", "AFGHANISTAN : {af}", "ALAND : {ax}", "ALBANIA : {al}", "ALGERIA : {dz}", "ANDORRA : {ad}", "ANGOLA : {ao}", "ANGUILLA : {ai}", "ANTARCTICA : {aq}", "ANTIGUA AND BARBUDA : {ag}", "ARGENTINA REPUBLIC : {ar}", "ARMENIA : {am}", "ARUBA : {aw}", "AUSTRALIA : {au}", "AUSTRIA : {at}", "AZERBAIJAN : {az}",
        "BAHAMAS : {bs}", "BAHRAIN : {bh}", "BANGLADESH : {bd}", "BARBADOS : {bb}", "BELARUS : {by}", "BELGIUM : {be}", "BELIZE : {bz}", "BENIN : {bj}", "BERMUDA : {bm}", "BHUTAN : {bt}", "BOLIVIA : {bo}", "BOSNIA AND HERZEGOVINA : {ba}", "BOTSWANA : {bw}", "BOUVET ISLAND : {bv}", "BRAZIL : {br}", "BRITISH INDIAN OCEAN TERR : {io}", "BRITISH VIRGIN ISLANDS : {vg}", "BRUNEI DARUSSALAM : {bn}", "BULGARIA : {bg}", "BURKINA FASO : {bf}", "BURUNDI : {bi}",         
        "CAMBODIA : {kh}", "CAMEROON : {cm}", "CANADA : {ca}", "CAPE VERDE : {cv}", "CAYMAN ISLANDS : {ky}", "CENTRAL AFRICAN REPUBLIC : {cf}", "CHAD : {td}", "CHILE : {cl}", "PEOPLE'S REPUBLIC OF CHINA : {cn}", "CHRISTMAS ISLANDS : {cx}", "COCOS ISLANDS : {cc}", "COLOMBIA : {co}", "COMORAS : {km}", "CONGO : {cg}", "CONGO (DEMOCRATIC REPUBLIC) : {cd}", "COOK ISLANDS : {ck}", "COSTA RICA : {cr}", "COTE D IVOIRE : {ci}", "CROATIA : {hr}", "CUBA : {cu}", "CYPRUS : {cy}", "CZECH REPUBLIC : {cz}",             
        "DENMARK : {dk}", "DJIBOUTI : {dj}", "DOMINICA : {dm}", "DOMINICAN REPUBLIC : {do}",
        "EAST TIMOR : {tp}", "ECUADOR : {ec}", "EGYPT : {eg}", "EL SALVADOR : {sv}", "EQUATORIAL GUINEA : {gq}", "ESTONIA : {ee}", "ETHIOPIA : {et}",
        "FALKLAND ISLANDS : {fk}", "FAROE ISLANDS : {fo}", "FIJI : {fj}", "FINLAND : {fi}", "FRANCE : {fr}", "FRANCE METROPOLITAN : {fx}", "FRENCH GUIANA : {gf}", "FRENCH POLYNESIA : {pf}", "FRENCH SOUTHERN TERRITORIES : {tf}",         
        "GABON : {ga}", "GAMBIA : {gm}", "GEORGIA : {ge}", "GERMANY : {de}", "GHANA : {gh}", "GIBRALTER : {gi}", "GREECE : {gr}", "GREENLAND : {gl}", "GRENADA : {gd}", "GUADELOUPE : {gp}", "GUAM : {gu}", "GUATEMALA : {gt}", "GUINEA : {gn}", "GUINEA-BISSAU : {gw}", "GUYANA : {gy}",
        "HAITI : {ht}", "MCDONALD ISLAND : {hm}", "HONDURAS : {hn}", "HONG KONG : {hk}", "HUNGARY : {hu}",
        "ICELAND : {is}", "INDIA : {in}", "INDONESIA : {id}", "ISLAMIC REPUBLIC OF IRAN : {ir}", "IRAQ : {iq}", "IRELAND : {ie}", "ISLE OF MAN : {im}", "ISRAEL : {il}", "ITALY : {it}",      
        "JAMAICA : {jm}", "JAPAN : {jp}", "JORDAN : {jo}",
        "KAZAKHSTAN : {kz}", "KENYA : {ke}", "KIRIBATI : {ki}", "DEM PEOPLES REP OF KOREA : {kp}", "REPUBLIC OF KOREA : {kr}", "KUWAIT : {kw}", "KYRGYZSTAN : {kg}",     
        "LAO PEOPLE'S DEM. REPUBLIC : {la}", "LATVIA : {lv}", "LEBANON : {lb}", "LESOTHO : {ls}", "LIBERIA : {lr}", "LIBYAN ARAB JAMAHIRIYA : {ly}", "LIECHTENSTEIN : {li}", "LITHUANIA : {lt}", "LUXEMBOURG : {lu}",
        "MACAO : {mo}", "MACEDONIA : {mk}", "MADAGASCAR : {mg}", "MALAWI : {mw}", "MALAYSIA : {my}", "MALDIVES : {mv}", "MALI : {ml}", "MALTA : {mt}", "MARSHALL ISLANDS : {mh}", "MARTINIQUE : {mq}", "MAURITANIA : {mr}", "MAURITIUS : {mu}", "MAYOTTE : {yt}", "MEXICO : {mx}", "MICRONESIA : {fm}", "REPUBLIC OF MOLDAVA : {md}", "MONACO : {mc}", "MONGOLIA : {mn}", "MONTENEGRO : {me}", "MONTSERRAT : {ms}", "MOROCCO : {ma}", "MOZAMBIQUE : {mz}", "MYANMAR : {mm}",
        "NAMIBIA : {na}", "NAURU : {nr}", "NEPAL : {np}", "NETHERLANDS ANTILLES : {an}", "THE NETHERLANDS : {nl}", "NEW CALEDONIA : {nc}", "NEW ZEALAND : {nz}", "NICARAGUA : {ni}", "NIGER : {ne}", "NIGERIA : {ng}", "NIUE : {nu}", "NORFOLK ISLAND : {nf}", "NORTHERN MARIANA ISLANDS : {mp}", "NORWAY : {no}",         
        "OMAN : {om}",
        "PAKISTAN : {pk}", "PALAU : {pw}", "PALESTINE : {ps}", "PANAMA : {pa}", "PAPUA NEW GUINEA : {pg}", "PARAGUAY : {py}", "PERU : {pe}", "REPUBLIC OF THE PHILIPPINES : {ph}", "PITCAIRN : {pn}", "POLAND : {pl}", "PORTUGAL : {pt}", "PUERTO RICO : {pr}",  
        "QATAR : {qa}",
        "REUNION : {re}", "ROMANIA : {ro}", "RUSSIAN FEDERATION : {ru}", "RWANDA : {rw}",
        "SAMOA : {ws}", "SAN MARINO : {sm}", "SAO TOME/PRINCIPE : {st}", "SAUDI ARABIA : {sa}", "SCOTLAND : {uk}", "SENEGAL : {sn}", "SERBIA : {rs}", "SEYCHELLES : {sc}", "SIERRA LEONE : {sl}", "SINGAPORE : {sg}", "SLOVAKIA : {sk}", "SLOVENIA : {si}", "SOLOMON ISLANDS : {sb}", "SOMALIA : {so}", "SOMOA,GILBERT,ELLICE ISLANDS : {as}", "SOUTH AFRICA : {za}", "SOUTH GEORGIA, SOUTH SANDWICH ISLANDS : {gs}", "SOVIET UNION : {su}", "SPAIN : {es}", "SRI LANKA : {lk}", "ST HELENA : {sh}", "ST KITTS AND NEVIS : {kn}", "ST LUCIA : {lc}", "ST PIERRE AND MIQUELON : {pm}", "ST VINCENT THE GRENADINES : {vc}", "SUDAN : {sd}", "SURINAME : {sr}", "SVALBARD AND JAN MAYEN : {sj}", "SWAZILAND : {sz}", "SWEDEN : {se}", "SWITZERLAND : {ch}", "SYRIAN ARAB REPUBLIC : {sy}",
        "TAIWAN : {tw}", "TAJIKISTAN : {tj}", "UNITED REPUBLIC OF TANZANIA : {tz}", "THAILAND : {th}", "TOGO : {tg}", "TOKELAU : {tk}", "TONGA : {to}", "TRINIDAD AND TOBAGO : {tt}", "TUNISIA : {tn}", "TURKEY : {tr}", "TURKMENISTAN : {tm}", "TURKS AND CALCOS ISLANDS : {tc}", "TUVALU : {tv}",            
        "UGANDA : {ug}", "UKRAINE : {ua}", "UNITED ARAB EMIRATES : {ae}", "UNITED KINGDOM (no new registrations) : {gb}", "UNITED KINGDOM : {uk}", "UNITED STATES : {us}", "UNITED STATES MINOR : {um}", "URUGUAY : {uy}", "UZBEKISTAN : {uz}",
        "VANUATU : {vu}", "VATICAN CITY STATE : {va}", "VENEZUELA : {ve}", "VIET NAM : {vn}", "VIRGIN ISLANDS (USA) : {vi}", 
        "WALLIS AND FUTUNA ISLANDS : {wf}", "WESTERN SAHARA : {eh}",            
        "YEMEN : {ye}",
        "ZAMBIA : {zm}", "ZIMBABWE : {zw}"
                ], multi_select=True, show_multi_select_hint=True,)
            
            menu_entry_indices = terminal_menu.show()
            print(colored('\nYour Exclude Nodes Configuration : \n', 'magenta'))
            print(terminal_menu.chosen_menu_entries)
            fichier = open("data/torrc.config.sh", "a")
            fichier.write(str(('\nExcludeNodes ' + ",".join([item.split(" : ")[1] for item in terminal_menu.chosen_menu_entries]))))
            fichier.close()
            anykay = input(colored("\nEnter anything to return to configuration menu : ", 'yellow'))
            Entry_Exit_Exclude()
    
    
    def Start_Torrc_Config():
        subprocess.call(['clear'], shell=True)
        print(colored(Start_Tor_Banner, 'magenta'))
        subprocess.call(['./bash_cmd/Shifting.sh'] , shell=True)
        print(colored('[+] Configuration file is on : /etc/tor ', 'green'))
        print(colored('[+] Now go to the menu to launch Tor', 'green'))
        anykay = input(colored("\nEnter anything to return to configuration menu : ", 'yellow'))
        Entry_Exit_Exclude()

    
    def Remove_Torrc_Config():
        subprocess.call(['clear'])
        print(colored(Entry_Nodes_Banner, 'magenta'))
        subprocess.call(['./bash_cmd/Remove_Torrc.sh'], shell=True)
        print(colored('[+] Configuration file is Remove ...', 'green'))
        anykay = input(colored("\nEnter anything to return to configuration menu : ", 'yellow'))
        Entry_Exit_Exclude()


    subprocess.call(['clear'], shell=True)
    Entry_Exit_Exclude()


def Check_IP():
    subprocess.call(['clear'], shell=True)
    print(colored(Check_IP_Banner, 'magenta'))
    print(colored('\n[+] Checking TOR... ', 'green' ))
    subprocess.call(['./bash_cmd/Test_Tor.sh'], shell=True)
    print(colored('\n[+] Checking IP ...\n', 'green'))
    print(colored(requests.get('http://httpbin.org/ip').text, 'green'))
    anykay = input(colored("\nEnter anything to return to main menu : ", 'yellow'))
    subprocess.call(['clear'], shell=True)
    MainMenu()


def Relay_Information():
    subprocess.call(['clear'], shell=True)
    subprocess.call(['./bash_cmd/Relay_Information.sh'], shell=True)
    subprocess.call(['clear'], shell=True)
    MainMenu()

def Search_Onion():
    
    # Dark Search

    subprocess.call(['clear'], shell=True)
    print(colored(Search_Onion_Banner, 'magenta'))
    print('\n')
    print(colored('To put a space between two words use : %20', 'yellow'))
    XQuery = input(colored("Please set your query : ", 'yellow'))
    print('\n')

    r = requests.get('https://darksearch.io/api/search?query=' + XQuery)
    data_json = r.text
    json_data = json.loads(data_json)

    #pages = json_data['last_page']
    #print(pages)
    for p in range(1,20):
        for i in range(0,2):
            try:
                url = 'https://darksearch.io/api/search?query=' + XQuery + '&page=' + str(p)
                r = requests.get(url)
                data_json = r.text
                json_data = json.loads(data_json)
                print(colored(json_data['data'][i]['link'], 'green'))
            except Exception as excep:
                print(excep)
    
    anykay = input(colored("Enter anything to return to main menu : ", 'yellow'))
    subprocess.call(['clear'], shell=True)
    MainMenu()               


def Quit():
    subprocess.call(['clear'], shell=True)
    exit()


Search_Onion_Banner = r'''
   _____                      __        ____        _           
  / ___/___  ____ ___________/ /_      / __ \____  (_)___  ____ 
  \__ \/ _ \/ __ `/ ___/ ___/ __ \    / / / / __ \/ / __ \/ __ \
 ___/ /  __/ /_/ / /  / /__/ / / /  _/ /_/ / / / / / /_/ / / / /
/____/\___/\__,_/_/   \___/_/ /_/  (_)____/_/ /_/_/\____/_/ /_/ 
'''                                                                

Main_Menu_Banner = r'''
    ___    ____   ____         ______          
   /   |  / / /  /  _/___     /_  __/___  _____
  / /| | / / /   / // __ \     / / / __ \/ ___/
 / ___ |/ / /  _/ // / / /    / / / /_/ / /    
/_/  |_/_/_/  /___/_/ /_/    /_/  \____/_/     
Twitter : @JeremGuillermin
'''

Entry_Nodes_Banner = r'''
   ______            _____                        __  _           
  / ____/___  ____  / __(_)___ ___  ___________ _/ /_(_)___  ____ 
 / /   / __ \/ __ \/ /_/ / __ `/ / / / ___/ __ `/ __/ / __ \/ __ \
/ /___/ /_/ / / / / __/ / /_/ / /_/ / /  / /_/ / /_/ / /_/ / / / /
\____/\____/_/ /_/_/ /_/\__, /\__,_/_/   \__,_/\__/_/\____/_/ /_/ 
                       /____/                                     
'''

Start_Tor_Banner = r'''
   _____ __             __     ______          
  / ___// /_____ ______/ /_   /_  __/___  _____
  \__ \/ __/ __ `/ ___/ __/    / / / __ \/ ___/
 ___/ / /_/ /_/ / /  / /_     / / / /_/ / /    
/____/\__/\__,_/_/   \__/    /_/  \____/_/                                                    
'''

Stop_Tor_Banner = r'''
   _____ __                 ______          
  / ___// /_____  ____     /_  __/___  _____
  \__ \/ __/ __ \/ __ \     / / / __ \/ ___/
 ___/ / /_/ /_/ / /_/ /    / / / /_/ / /    
/____/\__/\____/ .___/    /_/  \____/_/     
              /_/                           
'''

Check_IP_Banner = r'''
   ________              __      ________ 
  / ____/ /_  ___  _____/ /__   /  _/ __ \
 / /   / __ \/ _ \/ ___/ //_/   / // /_/ /
/ /___/ / / /  __/ /__/ ,<    _/ // ____/ 
\____/_/ /_/\___/\___/_/|_|  /___/_/      
'''                                          

MainMenu()