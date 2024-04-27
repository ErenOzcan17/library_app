class Ui:
    def __init__(self, menu_items):
        self.Menu_items = menu_items

    def Show_Menu(self):
        print("-"*50, "|{:*^50}|".format("MENÜ"), "-"*50, sep="\n")
        for no, item in enumerate(self.Menu_items):
            print("|{:^50}|".format(str(no+1)+"..."+item))
        print("-"*52)

    def GetChoise(self):
        try:
            choise = int(input(f"lütfen tercihinizi giriniz [1-{len(self.Menu_items)}]"))
            assert 1 <= choise <= len(self.Menu_items), f"lütfen tercihinizi giriniz [1-{len(self.Menu_items)}] arasında bir deger giriniz"
            return choise
        except AssertionError as e:
            print(e)

        except:
            print("hatalı giriş")
