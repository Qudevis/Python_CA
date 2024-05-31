# uz duomenu vaiksciojima ir panasiai


# import classes.knyga .... sukurti kelias knygas... susidedama i sarasa.... Tuomet sita sarasa galime siust i modules

# import from modules.... kvss.suskaiciuoti_vidutini(knygu_sarasas)

# modules book_saver (generic_saver) book_saver.save(book)

# modules.knygu_funkcijos as kf kf.create_book(Title,Author,Publish) (galetu is karto ir isaugoti)


# import Views.menu as mn
# import Views.knygu_saraas as ks
# pasirinkimas = mn.atspausdink_menu()
# while
#     match:
#         if pasirinkimas == 1.... # ATSPAUSDINK KNYGU SARASA
#             ks.kn_sar()

#         if pasirinkimas == 2 ...

#         pasirinkimas == 'q'
#             break
import modules.book_functions as bf
while True:
    match input("Pasirinkite veiksma: "):
        case "1": # perziureti knygas
            print("Peržiūrėti knygas") 
            bf.Show_Books()
            print("Aciu, kad perziurejot, kas toliau... ")
        case "q":
            break





