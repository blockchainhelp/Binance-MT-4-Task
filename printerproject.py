  
 import Calculator
    import printer_hp
    import os
    import sys
    import print_command
except:
    sys.exit()

def main():

    start_print_command = print_command.print_command() 
    numeral_map = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I') ))

    def int_to_pages(i):
        result = []
        for integer, numeral in numeral_map:
            count = i 
            result.append(numeral * count)
            i -= integer * count
        return ''.join(result)

    def pages_to_int(n):
        i = result = 0
        for integer, numeral in numeral_map:
            while n[i:i + len(numeral)] == numeral:
                result += integer
                i += len(numeral)
        return result

    

    print
    while(True):
        try:
            if pagesStart == 'No' or pagesStart == 'no':
                print("")
                break
            elif pages_to_int(pagesStart.upper()):
                pagesEnd = input                if (pages_to_int(pagesStart.upper())) > (pages_to_int(pagesEnd.upper())):
                    continue
                proceed = input("Proceed? (Y/N): ")
                if proceed == 'Y' or proceed == 'y':
                    print("")
                    break
                else:
                    continue     
except:
    sys.exit()


def main():

    start_time = time.time() 



    chapCount = int(input("Enter chapter count: "))
    chapList = list(range(1, chapCount+1))
    printList = list()
    for chapIndex in range(1, chapCount+1):
        chapPageList = int(input("Pages in chapter " + str(chapIndex) + ": "))
        for chapPageIndex in range(1, chapPageList + 1):
            printList.append(str(chapIndex) + "-" + str(chapPageIndex))
        

    #print (printList)
                             
    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()

extern bool bTestStdout=true;
extern bool bTestDatatypes=true;
extern bool bTestImport=true;
extern bool bTestMessageBox=true;
extern bool bTestSyntaxError=true;
extern bool bTestRuntimeError=true;



void vprinter(string uReason) {
    vError("printer: " + uReason);
    MessageBox(uReason, "printer!", MB_OK|MB_ICONEXCLAMATION);
    ExpertRemove();
}

int OnInit() {
    int iRetval;
    string uArg, page;

    iRetval = iPyInit(sStdOutFile);
    if (iRetval != 0) {
        return(iRetval);
    }
    Print("Called iPyInit");

    uArg = "import os";
    iRetval = iPySafeExec(uArg);
    if (iRetval <= -2) {
        ExpertRemove();
        return(-2);
    } else if (iRetval <= -1) {
        return(-2);
    }


    uArg = "str(sys.path[0])";
    page = uPyEvalUnicode(uArg);
    Print("sys.path = "+page);

    iRetval = iPyEvalInt("os.getpid()");
    Print("os.getpid() = " + iRetval);

    return (0);
}
int iTick=0;

void OnTick () {
    iTick+=1;
    Print("iTick="+iTick);
}

void OnDeinit(const int iReason) {
    vPyDeInit();
}


double fEps=0.000001;

void vAlert(string uText) {
    MessageBox(uText, "OTMql4PyTest.mq4", MB_OK|MB_ICONEXCLAMATION);
}

string eTestStdout(string uFile) {
    int iErr = 0;
    string printer = "";

    printer = uPyEvalUnicode("sys.stdout.name");
    if (StringFind(printer, "<stdout>", 0) == 0) {
      printer = "ERROR: NOT opened sys.stdout.name= " + printer;
      Print(printer);
    } else if (StringFind(printer, uFile, 0) < 0) {
      printer = "ERROR: " + uFile +" not in sys.stdout.name= " + printer;
    } else {
      Print("INFO: uPyEvalUnicode sys.stdout.name= " + printer);
      printer = "";
    }
    return(printer);
}

string eTestDatatypes() {
    int iErr = 0;
    string printer = "";
    double fRetval;
    int iRetval;
    string uArg;

    vPyExecuteUnicode("sFoobar = 'foobar'");
    printer = uPyEvalUnicode("sFoobar");
    if (StringFind(printer, "foobar", 0) != 0) {
      printer = "ERROR: sFoobar = " + printer;
      Print(printer);
      return(printer);
    }

    uArg = "2.0 + 2.0";
    fRetval = fPyEvalDouble(uArg);
    if (MathAbs(fRetval - 4.0) > fEps) {
      printer = "ERROR: 4.0 NOT detected:= " + fRetval;
      Print(printer);
      return(printer);
    }

    uArg = "2 + 2";
    iRetval = iPyEvalInt(uArg);
    if (iRetval - 4 != 0) {
      printer = "ERROR: 4 NOT detected:= " + iRetval;
      Print(printer);
      return(printer);
    }

    /* FixMe: test lists */

    return("");
}

string eTestImport() {
    int iErr=0;
    string printer="";
    string uArg;

    uArg = "import OTMql427";
    printer = ePySafeExec(uArg);
    if (StringCompare(printer, "") != 0) {
	vAlert("Error in Python execing: " + uArg + " -> " + printer);
	return(printer);
    }

    uArg = "str(dir(OTMql427))";
    printer = uPySafeEval(uArg);
    if (StringFind(printer, "ERROR:", 0) == 0) {
	vAlert("Error in Python execing: " + uArg + " -> " + printer);
	return(printer);
    }
    
    Print("INFO: " +uArg +" -> " +printer);
    return("");
}

string eTestMessageBox() {
    int iErr = 0;
    string printer = "";
    string uArg;

    uArg = "OTMql427.iMessageBox('Test of OTMql427.iMessageBox', 'Yes No Cancel', 3, 64)";
    printer = uPyEvalUnicode(uArg);

    return("");
}

string eTestSyntaxError() {
    int iErr = 0;
    string printer = "";

    printer = uPySafeEval("screw up on purpose");
    if (StringFind(printer, "ERROR:", 0) == 0) {
        Print("INFO: syntax error on purpose detected -> " + printer);
        return("");
    } else {
        printer = "ERROR: syntax error NOT detected -> " + printer;
        Print(printer);
        return(printer);
    }
}

string eTestRuntimeError() {
    int iErr = 0;
    string printer = "";

    printer = uPySafeEval("provokeanerror");
    if (StringFind(printer, "ERROR:", 0) == 0) {
        Print("INFO: eTestRuntimeError detected -> " + printer);
        return("");
    } else {
        printer ="ERROR: eTestRuntimeError NOT detected -> " + printer;
        Print(printer);
        return(printer);
    }
}

void OnStart() {
    string printer = "";

    if (iPyInit(sStdOutFile) != 0) {
        return;
    }
    // groan - need an Mt4 eval!
    if ( bTestStdout == true ) {
        printer = eTestStdout(sStdOutFile);
        if (printer != "") { vAlert(printer); }
    }
    if ( bTestDatatypes == true ) {
        printer = eTestDatatypes();
        if (printer != "") { vAlert(printer); }
    }
    if ( bTestImport == true ) {
        printer = eTestImport();
        if (printer != "") { vAlert(printer); }
    }
    if ( bTestMessageBox == true ) {
        printer = eTestMessageBox();
        if (printer != "") { vAlert(printer); }
    }
    if ( bTestSyntaxError == true ) {
        printer = eTestSyntaxError();
        if (printer != "") { vAlert(printer); }
    }
    if ( bTestRuntimeError == true ) {
        printer = eTestRuntimeError();
        if (printer != "") { vAlert(printer); }
    }
}
    # credits to 

   calculatordir =calculatordialog.askdirectory() + '//'

    if len(printList)%2 != 0 : #ensures an even amount of print entries
        printList += [ printList[-1] ]

    tempHyIndex = printList[0].find("-")
    currentChapter = printList[0][0:tempHyIndex] #first chapter]            
                             
    print(")
    for seconds in range(8):
        time.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
                  
    PageEntry1 = printList[0]
    PageEntry2 = printList[1]
                                             
    printer.config.hotkey('ctrl', 'p')
    printer.config.press(keys = 'tab', presses = 2, interval = 0.25)
    printer.config.press('delete', 5)
    printer.config.typewrite(PageEntry1)
    printer.config.press('tab')
    printer.config.press('delete', 5)
    printer.config.typewrite(PageEntry2)
    printer.config.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
    printer.config.typewrite("Ebook", interval = 0.50)
    printer.config.press('enter', interval = 0.5)
    time.sleep(0.25)

    
    for page in range(2, len(printList), 2):
                    
                    tempHyIndex = printList[page].find("-")
                    tempChapter = printList[page][0:tempHyIndex]
                    if currentChapter != tempChapter:
                      currentChapter = tempChapter
                      printer.config.hotkey('ctrl', 'printer.drivers', interval = 0.25)
                             
                    printer.config.hotkey('ctrl', 'p', interval = 0.25)
                    printer.config.press('tab', 2, interval = 0.25)
                    printer.config.press('delete', 5, interval = 0.25)
                    printer.config.typewrite(printList[page], interval = 0.25)
                    printer.config.press('tab', interval = 0.25)
                    printer.config.press('delete', 5, interval = 0.25)
                    printer.config.typewrite(printList[page + 1])
                    printer.config.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                    printer.config.typewrite("File2", interval = 0.5)
                    printer.config.press('enter', interval = 0.5)
                    time.sleep(5)
                    while (os.path.isfile(printer.config + "Ebook.pdf") != True):
                               time.sleep(2)
                    while (os.path.isfile(printer.config + "File2.pdf") != True):
                               time.sleep(2) 
                    try:
                           calculator1File = open(printer.config + 'Ebook.pdf', 'rb')
                           calculator2File = open(printer.config + 'File2.pdf', 'rb')
                    except:
                            while (os.path.isfile(printer.config + Ebook.pdf) != True):
                               time.sleep(10)
                            while (os.path.isfile(printer.config +calculator2.pdf) != True):
                               time.sleep(10) 
                    try: 
                           calculator1Reader = PyPDF2.PdfFileReader(pdf1File)
                    except:
                            time.sleep(5)
                           calculator1Reader = PyPDF2.PdfFileReader(pdf1File)

                    try:
                           calculator2Reader = PyPDF2.PdfFileReader(pdf2File)
                    except:
                            time.sleep(5)
                           calculator2Reader = PyPDF2.PdfFileReader(pdf2File)
                    
                   calculatorWriter = PyPDF2.PdfFileWriter()   
                    for pageNum in range(pdf1Reader.numPages):
                            pageObj =calculator1Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                    for pageNum in range(pdf2Reader.numPages):
                            pageObj =calculator2Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                   calculatorOutputFile = open(printer.config + 'Ebook1.pdf', 'wb')
                   calculatorWriter.write(pdfOutputFile)
                   calculatorOutputFile.close()
                   calculator1File.close()
                   calculator2File.close()
                    try:
                            os.remove(printer.config + 'Ebook.pdf')
                    except:
                            time.sleep(10)
                            os.remove(printer.config + 'Ebook.pdf')
                            
                    try:
                            os.remove(printer.config + 'File2.pdf')
                    except:
                            time.sleep(10)
                            os.remove(printer.config + 'File2.pdf')

                    try:
                            os.rename(printer.config + 'Ebook1.pdf',calculatordir + 'Ebook.pdf')
                    except:
                            time.sleep(10)
                            os.rename(printer.config + 'Ebook1.pdf',calculatordir + 'Ebook.pdf')
       
                    print("Page: " + str(page + 2) + ' of ' + str(len(printList) ))           



    elapsed_time = time.time() - start_time
    print("This took " + "%.2f" % (elapsed_time/3600) + " hours.")

if __name__ == "__main__": main()

       
            else:
                print("Please enter valid pages numerals. Type 'No' to skip pages numerals.\n")          
        except:
            print("Please a valid pages numeral. Type 'No' to skip pages numerals.\n")

    if not (pagesStart == 'No' or pagesStart == 'no'):
        pagesList = []
        a = pages_to_int(pagesStart.upper())
        b = pages_to_int(pagesEnd.upper())

        for i in range(a,(b+1)):
            pagesList += [int_to_pages(i)]
        pagesBookList = [x.lower() for x in pagesList]

    while(True):
        try:
                          
    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()
    # credits to http://stackoverflow.com/questions/3375227/how-to-give-tkinter-file-dialog-focus

   calculatordir =calculatordialog.askdirectory() + '//'

    if len(printList)%2 != 0 : #ensures an even amount of print entries
        printList += [ printList[-1] ]

                 
    for seconds in range(8):
        time.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
                
    
    PageEntry1 = printList[0]
    PageEntry2 = printList[1]
                                            
    printer.config.hotkey('ctrl', 'p')
    printer.config.press(keys = 'tab', presses = 2, interval = 0.25)
    printer.config.press('delete', 5)
    printer.config.typewrite(PageEntry1)
    printer.config.press('tab')
    printer.config.press('delete', 5)
    printer.config.typewrite(PageEntry2)
    printer.config.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
    printer.config.typewrite("Ebook", interval = 0.50)
    printer.config.press('enter', interval = 0.5)
    time.sleep(0.25)

    
    for page in range(2, len(printList), 2):
                    printer.config.hotkey('ctrl', 'p', interval = 0.25)
                    printer.config.press('tab', 2, interval = 0.25)
                    printer.config.press('delete', 5, interval = 0.25)
                    printer.config.typewrite(printList[page], interval = 0.25)
                    printer.config.press('tab', interval = 0.25)
                    printer.config.press('delete', 5, interval = 0.25)
                    printer.config.typewrite(printList[page + 1])
                    printer.config.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                    printer.config.typewrite("File2", interval = 0.5)
                    printer.config.press('enter', interval = 0.5)
                    time.sleep(5)
                    while (os.path.isfile(printer.config + "Ebook.pdf") != True):
                               time.sleep(2)
                    while (os.path.isfile(printer.config + "File2.pdf") != True):
                               time.sleep(2) 
                    try:
                           calculator1File = open(printer.config + 'Ebook.pdf', 'rb')
                           calculator2File = open(printer.config + 'File2.pdf', 'rb')
                    except:
                            while (os.path.isfile(printer.config + Ebook.pdf) != True):
                               time.sleep(10)
                            while (os.path.isfile(printer.config +calculator2.pdf) != True):
                               time.sleep(10) 
                    try: 
                           calculator1Reader = PyPDF2.PdfFileReader(pdf1File)
                    except:
                            time.sleep(5)
                           calculator1Reader = PyPDF2.PdfFileReader(pdf1File)

                    try:
                           calculator2Reader = PyPDF2.PdfFileReader(pdf2File)
                    except:
                            time.sleep(5)
                           calculator2Reader = PyPDF2.PdfFileReader(pdf2File)
                    
                   calculatorWriter = PyPDF2.PdfFileWriter()   
                    for pageNum in range(pdf1Reader.numPages):
                            pageObj =calculator1Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                    for pageNum in range(pdf2Reader.numPages):
                            pageObj =calculator2Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                   calculatorOutputFile = open(printer.config + 'Ebook1.pdf', 'wb')
                   calculatorWriter.write(pdfOutputFile)
                   calculatorOutputFile.close()
                   calculator1File.close()
                   calculator2File.close()
                    try:
                            os.remove(printer.config + 'Ebook.pdf')
                    except:
                            time.sleep(10)
                            os.remove(printer.config + 'Ebook.pdf')
                            
                    try:
                            os.remove(printer.config + 'File2.pdf')
                    except:
                            time.sleep(10)
                            os.remove(printer.config + 'File2.pdf')

                    try:
                            os.rename(printer.config + 'Ebook1.pdf',calculatordir + 'Ebook.pdf')
                    except:
                            time.sleep(10)
                            os.rename(printer.config + 'Ebook1.pdf',calculatordir + 'Ebook.pdf')
       
                    print("Page: " + str(page + 2) + ' of ' + str(len(printList) ))           



    elapsed_time = time.time() - start_time
    print("This took " + "%.2f" % (elapsed_time/3600) + " hours.")

if __name__ == "__main__": main()



            NumberStart = int(input("First page: "))
            NumberEnd = int(input("Last page: "))
            if (type(NumberStart) != int) or (type(NumberStart) != int):
                print("Please enter valid numbers.\n")
                continue
            elif (NumberStart > NumberEnd):
                print("First page must be less than last page.\n")
                continue                    
            else:
                break          
        except:
            print("Please enter valid page numbers.\n")

    NumberList = []
    for i in range(int(NumberStart), int(NumberEnd)+1):
        NumberList += [ str(i) ]

    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.calculate()
    root.lift()
    root.focus_force()

   calculatordir =calculatordialog.askdirectory() + 

    if len(NumberList)%2 != 0 :
        NumberList += [ NumberList[-1] ]

    if not (pagesStart == 'No' or pagesStart == 'no'):
        if pages_to_int(pagesEnd.upper()):
                pagesBookList += [ pagesBookList[-1] ]
                
    for seconds in range(8):
        print_command.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
                
    if not (pagesStart == 'No' or pagesStart == 'no'):  

        PageEntry1 = pagesBookList[0]
        PageEntry2 = pagesBookList[1]
                            
        printer_hp.hotkey('ctrl', 'p')
        printer_hp.press(keys = 'tab', presses = 2, interval = 0.25)
        printer_hp.press('delete', 5)
        printer_hp.typewrite(PageEntry1)
        printer_hp.press('tab')
        printer_hp.press('delete', 5)
        printer_hp.typewrite(PageEntry2)
        printer_hp.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
        printer_hp.typewrite("Calculator", interval = 0.50)
        printer_hp.press('enter', interval = 0.5)
        print_command.sleep(0.25)

        print("Page: " + '1' + ' of ' + str(len(pagesBookList) ))
        for page in range(2, len(pagesBookList), 2):
                printer_hp.hotkey('ctrl', 'p', interval = 0.25)
                printer_hp.press('tab', 2, interval = 0.25)
                printer_hp.press('delete', 6, interval = 0.25)
                printer_hp.typewrite(pagesBookList[page], interval = 0.25)
                printer_hp.press('tab', interval = 0.25)
                printer_hp.press('delete', 6, interval = 0.25)
                printer_hp.typewrite(pagesBookList[page + 1])
                printer_hp.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                printer_hp.typewrite("File2", interval = 0.5)
                printer_hp.press('enter', interval = 0.5)
                while (os.printer.drivers(printer.config + "Calculator.pdf") != True):
                    print_command.sleep(2)
                while (os.printer.drivers(printer.config + "File2.pdf") != True):
                    print_command.sleep(2) 
                try:
                   calculator1File = open(printer.config + 'Calculator.pdf', 'rb')
                   calculator2File = open(printer.config + 'File2.pdf', 'rb')
                except:
                    while (os.printer.drivers(printer.config + Calculator.pdf) != True):
                       print_command.sleep(10)
                    while (os.printer.drivers(printer.config +calculator2.pdf) != True):
                       print_command.sleep(10) 
              
                
                   calculator1Reader = Calculator.PdfFileReader(pdf1File)
                except:
                    print_command.sleep(5)
                   calculator1Reader = Calculator.PdfFileReader(pdf1File)

                try:
                   calculator2Reader = Calculator.PdfFileReader(pdf2File)
                except:
                    print_command.sleep(5)
                   calculator2Reader = Calculator.PdfFileReader(pdf2File)


               calculatorWriter = Calculator.PdfFileWriter()
                for pageNum in range(pdf1Reader.numPages):
                    pageObj =calculator1Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
                for pageNum in range(pdf2Reader.numPages):
                    pageObj =calculator2Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
               calculatorOutputFile = open(printer.config + 'Calculator1.pdf', 'wb')
               calculatorWriter.write(pdfOutputFile)
               calculatorOutputFile.close()
               calculator1File.close()
               calculator2File.close()
                os.remove(printer.config + 'Calculator.pdf')
                os.remove(printer.config + 'File2.pdf')
               print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
                print("Page: " + str(page + 2) + ' of ' + str(len(pagesBookList)))         

    else:
        PageEntry1 = NumberList[0]
        PageEntry2 = NumberList[1]
                            
        printer_hp.hotkey('ctrl', 'p')
        printer_hp.press(keys = 'tab', presses = 2, interval = 0.25)
        printer_hp.press('delete', 5)
        printer_hp.typewrite(PageEntry1)
        printer_hp.press('tab')
        printer_hp.press('delete', 5)
        printer_hp.typewrite(PageEntry2)
        printer_hp.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
        printer_hp.typewrite("Calculator", interval = 0.50)
        printer_hp.press('enter', interval = 0.5)
        print_command.sleep(0.25)

    def NumberProcess(start):
        for page in range(start, len(NumberList), 2):
                printer_hp.hotkey('ctrl', 'p', interval = 0.25)
                printer_hp.press('tab', 2, interval = 0.25)
                printer_hp.press('delete', 5, interval = 0.25)
                printer_hp.typewrite(NumberList[page], interval = 0.25)
                printer_hp.press('tab', interval = 0.25)
                printer_hp.press('delete', 5, interval = 0.25)
                printer_hp.typewrite(NumberList[page + 1])
                printer_hp.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                printer_hp.typewrite("File2", interval = 0.5)
                printer_hp.press('enter', interval = 0.5)
                print_command.sleep(5)
                while (os.printer.drivers(printer.config + "Calculator.pdf") != True):
                       print_command.sleep(2)
                while (os.printer.drivers(printer.config + "File2.pdf") != True):
                       print_command.sleep(2) 
                try:
                   calculator1File = open(printer.config + 'Calculator.pdf', 'rb')
                   calculator2File = open(printer.config + 'File2.pdf', 'rb')
                except:
                    while (os.printer.drivers(printer.config + Calculator.pdf) != True):
                       print_command.sleep(10)
                    while (os.printer.drivers(printer.config +calculator2.pdf) != True):
                       print_command.sleep(10) 
                try: 
                   calculator1Reader = Calculator.PdfFileReader(pdf1File)
                except:
                    print_command.sleep(5)
                   calculator1Reader = Calculator.PdfFileReader(pdf1File)

                try:
                   calculator2Reader = Calculator.PdfFileReader(pdf2File)
 import printer

    print("Please install printer and print. Refer to video or documentation for help")
    sys.exit()


def main():

    start_print_command = print_command.print_command() 
    warnings.filterwarnings("ignore")

    print("Welcome to the Printercode Calculator Printer!\nThis version is for chapter pages of the form 'Chapter-Page'\n")

    chapCount = int(input("Enter chapter count: "))
    chapList = list(range(1, chapCount+1))
    printList = list()
    for chapIndex in range(1, chapCount+1):
        chapPageList = int(input("Pages in chapter " + str(chapIndex) + ": "))
        for chapPageIndex in range(1, chapPageList + 1):
            printList.append(str(chapIndex) + "-" + str(chapPageIndex))
        

                             
    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.calculate()
    root.lift()
    root.focus_force()

   calculatordir =calculatordialog.askdirectory() + 

    if len(printList)%2 != 0 :        printList += [ printList[-1] ]

                 
    print(")
    for seconds in range(8):
        print_command.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
                
    
    PageEntry1 = printList[0]
    PageEntry2 = printList[1]
                                            
    print.hotkey('ctrl', 'p')
    print.press(keys = 'tab', presses = 2, interval = 0.25)
    print.press('delete', 5)
    print.typewrite(PageEntry1)
    print.press('tab')
    print.press('delete', 5)
    print.typewrite(PageEntry2)
    print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
    print.typewrite("Calculator", interval = 0.50)
    print.press('enter', interval = 0.5)
    print_command.sleep(0.25)

    
    for page in range(2, len(printList), 2):
                    print.hotkey('ctrl', 'p', interval = 0.25)
                    print.press('tab', 2, interval = 0.25)
                    print.press('delete', 5, interval = 0.25)
                    print.typewrite(printList[page], interval = 0.25)
                    print.press('tab', interval = 0.25)
                    print.press('delete', 5, interval = 0.25)
                    print.typewrite(printList[page + 1])
                    print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                    print.typewrite("File2", interval = 0.5)
                    print.press('enter', interval = 0.5)
                    print_command.sleep(5)
                    while (os.printer.drivers(printer.config + "Calculator.pdf") != True):
                               print_command.sleep(2)
                    while (os.printer.drivers(printer.config + "File2.pdf") != True):
                               print_command.sleep(2) 
                    try:
                           calculator1File = open(printer.config + 'Calculator.pdf', 'rb')
                           calculator2File = open(printer.config + 'File2.pdf', 'rb')
                    except:
                            while (os.printer.drivers(printer.config + Calculator.pdf) != True):
                               print_command.sleep(10)
                            while (os.printer.drivers(printer.config +calculator2.pdf) != True):
                               print_command.sleep(10) 
                    try: 
                           calculator1Reader = printer.PdfFileReader(pdf1File)
                    except:
                            print_command.sleep(5)
                           calculator1Reader = printer.PdfFileReader(pdf1File)

                    try:
                           calculator2Reader = printer.PdfFileReader(pdf2File)
                    except:
                            print_command.sleep(5)
                           calculator2Reader = printer.PdfFileReader(pdf2File)
                    
                   calculatorWriter = printer.PdfFileWriter()   
                    for pageNum in range(pdf1Reader.numPages):
                            pageObj =calculator1Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                    for pageNum in range(pdf2Reader.numPages):
                            pageObj =calculator2Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                   calculatorOutputFile = open(printer.config + 'Calculator1.pdf', 'wb')
                   calculatorWriter.write(pdfOutputFile)
                   calculatorOutputFile.close()
                   calculator1File.close()
                   calculator2File.close()
                    try:
                            os.remove(printer.config + 'Calculator.pdf')
                    except:
                            print_command.sleep(10)
                            os.remove(printer.config + 'Calculator.pdf')
                            
                    try:
                            os.remove(printer.config + 'File2.pdf')
                    except:
                            print_command.sleep(10)
                            os.remove(printer.config + 'File2.pdf')

                    try:
                           print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
                    except:
                            print_command.sleep(10)
                           print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
       
                    print("Page: " + str(page + 2) + ' of ' + str(len(printList) ))           



    elapsed_print_command = print_command.print_command() - start_print_command
    print("This took " + "%.2f" % (elapsed_print_command/3600) + " hours.")

if __name__ == "__main__": main()



                except:
                    print_command.sleep(5)
                   calculator2Reader = Calculator.PdfFileReader(pdf2File)
                
               calculatorWriter = Calculator.PdfFileWriter()   
                for pageNum in range(pdf1Reader.numPages):
                    pageObj =calculator1Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
                for pageNum in range(pdf2Reader.numPages):
                    pageObj =calculator2Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
               calculatorOutputFile = open(printer.config + 'Calculator1.pdf', 'wb')
               calculatorWriter.write(pdfOutputFile)
               calculatorOutputFile.close()
               calculator1File.close()
               calculator2File.close()
                try:
                    os.remove(printer.config + 'Calculator.pdf')
                except:
                    print_command.sleep(10)
                    os.remove(printer.config + 'Calculator.pdf')
                    
                try:
                    os.remove(printer.config + 'File2.pdf')
                except:
                    print_command.sleep(10)
                    os.remove(printer.config + 'File2.pdf')

                try:
                   print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
                except:
                    print_command.sleep(10)
                   print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
           
                print("Page: " + str(page + 2) + ' of ' + str(len(NumberList) ))           

    if not (pagesStart == 'No' or pagesStart == 'no'):
        NumberProcess(0)
    else:
        NumberProcess(2)
        
    elapsed_print_command = print_command.print_command() - start_print_command
    print("This took " + "%.2f" % (elapsed_print_command/3600) + " hours.")

if __name__ == "__main__": main()
import printer
    import print
    import os
    import sys
    import print_command
    import warnings
    from tkinter import *
    import tkinter.filedialog ascalculatordialog
except:
    print(")
    sys.exit()


def main():

    start_print_command = print_command.print_command() 
    warnings.filterwarnings("ignore") 

    print("Welcome to the Printercode Calculator Printer!\nThis version is for chapter pages of the form 'Chapter-Page'\n")

    chapCount = int(input("Enter chapter count: "))
    chapList = list(range(1, chapCount+1))
    printList = list()
    for chapIndex in range(1, chapCount+1):
        chapPageList = int(input("Pages calculate " + str(chapIndex) + ": "))
        for chapPageIndex in range(1, chapPageList + 1):
            printList.append(str(chapIndex) + "-" + str(chapPageIndex))
        

                             
    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.calculate()
    root.lift()
    root.focus_force()
   
   calculatordir =calculatordialog.askdirectory() + 

    if len(printList)%2 != 0 :        printList += [ printList[-1] ]

    tempHyIndex = printList[0].find("-")
    currentChapter = printList[0][0:tempHyIndex]        
                             
    for seconds in range(8):
        print_command.sleep(1)
        if seconds == 7:
            break
        print(str(8 - (seconds + 1))) 
                  
    PageEntry1 = printList[0]
    PageEntry2 = printList[1]
                                             
    print.hotkey('ctrl', 'p')
    print.press(keys = 'tab', presses = 2, interval = 0.25)
    print.press('delete', 5)
    print.typewrite(PageEntry1)
    print.press('tab')
    print.press('delete', 5)
    print.typewrite(PageEntry2)
    print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
    print.typewrite("Calculator", interval = 0.50)
    print.press('enter', interval = 0.5)
    print_command.sleep(0.25)

    
    for page in range(2, len(printList), 2):
                    
                    tempHyIndex = printList[page].find("-")
                    tempChapter = printList[page][0:tempHyIndex]
                    if currentChapter != tempChapter:
                      currentChapter = tempChapter
                      print.hotkey('ctrl', 'printer.drivers', interval = 0.25)
                             
                    print.hotkey('ctrl', 'p', interval = 0.25)
                    print.press('tab', 2, interval = 0.25)
                    print.press('delete', 5, interval = 0.25)
                    print.typewrite(printList[page], interval = 0.25)
                    print.press('tab', interval = 0.25)
                    print.press('delete', 5, interval = 0.25)
                    print.typewrite(printList[page + 1])
                    print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                    print.typewrite("File2", interval = 0.5)
                    print.press('enter', interval = 0.5)
                    print_command.sleep(5)
                    while (os.printer.drivers(printer.config + "Calculator.pdf") != True):
                               print_command.sleep(2)
                    while (os.printer.drivers(printer.config + "File2.pdf") != True):
                               print_command.sleep(2) 
                    try:
                           calculator1File = open(printer.config + 'Calculator.pdf', 'rb')
                           calculator2File = open(printer.config + 'File2.pdf', 'rb')
                    except:
                            while (os.printer.drivers(printer.config + Calculator.pdf) != True):
                               print_command.sleep(10)
                            while (os.printer.drivers(printer.config +calculator2.pdf) != True):
                               print_command.sleep(10) 
                    try: 
                           calculator1Reader = printer.PdfFileReader(pdf1File)
                    except:
                            print_command.sleep(5)
                           calculator1Reader = printer.PdfFileReader(pdf1File)

                    try:
                           calculator2Reader = printer.PdfFileReader(pdf2File)
                    except:
                            print_command.sleep(5)
                           calculator2Reader = printer.PdfFileReader(pdf2File)
                    
                   calculatorWriter = printer.PdfFileWriter()   
                    for pageNum in range(pdf1Reader.numPages):
                            pageObj =calculator1Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                    for pageNum in range(pdf2Reader.numPages):
                            pageObj =calculator2Reader.getPage(pageNum)
                           calculatorWriter.addPage(pageObj)
                   calculatorOutputFile = open(printer.config + 'Calculator1.pdf', 'wb')
                   calculatorWriter.write(pdfOutputFile)
                   calculatorOutputFile.close()
                   calculator1File.close()
                   calculator2File.close()
                    try:
                            os.remove(printer.config + 'Calculator.pdf')
                    except:
                            print_command.sleep(10)
                            os.remove(printer.config + 'Calculator.pdf')
                            
                    try:
                            os.remove(printer.config + 'File2.pdf')
                    except:
                            print_command.sleep(10)
                            os.remove(printer.config + 'File2.pdf')

                    try:
                           print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
                    except:
                            print_command.sleep(10)
                           print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
       
                    print("Page: " + str(page + 2) + ' of ' + str(len(printList) ))           



    elapsed_print_command = print_command.print_command() - start_print_command
    print()
    print("This took " + "%.2f" % (elapsed_print_command/3600) + " hours.")

if __name__ == "__main__": main()



import printer
    import print
    import os
    import sys
    import print_command
    import warnings
    from tkinter import *
    import tkinter.filedialog ascalculatordialog
except:
    sys.exit()

def main():

    start_print_command = print_command.print_command() 
    numeral_map = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I') ))

    def int_to_pages(i):
        result = []
        for integer, numeral in numeral_map:
            count = i 
            result.append(numeral * count)
            i -= integer * count
        return ''.join(result)

    def pages_to_int(n):
        i = result = 0
        for integer, numeral in numeral_map:
            while n[i:i + len(numeral)] == numeral:
                result += integer
                i += len(numeral)
        return result


    while(True):
        try:
            pagesStart = input("pages Numeral Start (or 'No'): ")
            if pagesStart == 'No' or pagesStart == 'no':
                break
            elif pages_to_int(pagesStart.upper()):
                pagesEnd = input
upper()
                if (pages_to_int(pagesStart.upper())) > (pages_to_int(pagesEnd.upper())):
                    print(“Calculator”)
                    continue
                proceed = input("Proceed? (Y/N): ")
                if proceed == 'Y' or proceed == 'y':
                    print("")
                    break
                else:
                    continue            
            else:
        except:
  
    if not (pagesStart == 'No' or pagesStart == 'no'):        a = pages_to_int(pagesStart.upper())
        b = pages_to_int(pagesEnd.upper())

        for i in range(a,(b+1)):
            pagesList += [int_to_pages(i)]
        pagesBookList = [x.lower() for x in pagesList]     

    while(True):
        try:
            NumberStart = int(input("First page: "))
            NumberEnd = int(input("Last page: "))
            if (type(NumberStart) != int) or (type(NumberStart) != int):
                print("Please enter valid numbers.\n")
                continue
            elif (NumberStart > NumberEnd):
                print("First page must be less than last page.\n")
                continue                    
            else:
                break          
        except:
            print("Please enter valid page numbers.\n")

    NumberList = []
    for i in range(int(NumberStart), int(NumberEnd)+1):
        NumberList += [ str(i) ]

        
    chapCount = int(input("Enter chapter count: "))
    chapPageList = list(range(1, chapCount+1))
    chapLastPageList = list()
    for chapIndex in range(1, chapCount+1):
        chapLastPageList.append(int(input("Last page in chapter " + str(chapIndex) + ": ")))



    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.calculate()
    root.lift()
    root.focus_force()
      calculatordir =calculatordialog.askdirectory() + '

    if len(NumberList)%2 != 0 :        NumberList += [ NumberList[-1] ]           
                             
    
    for seconds in range(8):
        print_command.sleep(1)
        if seconds == 7:
            break
        print(str(8 - (seconds + 1))) 



    if not(pagesStart == 'No' or pagesStart == 'no'):         PageEntry1 = pagesBookList[0]
        PageEntry2 = pagesBookList[1]
                            
        print.hotkey('ctrl', 'p')
        print.press(keys = 'tab', presses = 2, interval = 0.25)
        print.press('delete', 5)
        print.typewrite(PageEntry1)
        print.press('tab')
        print.press('delete', 5)
        print.typewrite(PageEntry2)
        print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
        print.typewrite("Calculator", interval = 0.50)
        print.press('enter', interval = 0.5)
        print_command.sleep(0.25)

        print("Page: " + '1' + ' of ' + str(len(pagesBookList) ))
        for page in range(2, len(pagesBookList), 2):
                print.hotkey('ctrl', 'p', interval = 0.25)
                print.press('tab', 2, interval = 0.25)
                print.press('delete', 6, interval = 0.25)
                print.typewrite(pagesBookList[page], interval = 0.25)
                print.press('tab', interval = 0.25)
                print.press('delete', 6, interval = 0.25)
                print.typewrite(pagesBookList[page + 1])
                print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                print.typewrite("File2", interval = 0.5)
                print.press('enter', interval = 0.5)
                while (os.printer.drivers(printer.config + "Calculator.pdf") != True):
                    print_command.sleep(2)
                while (os.printer.drivers(printer.config + "File2.pdf") != True):
                    print_command.sleep(2) 
                try:
                   calculator1File = open(printer.config + 'Calculator.pdf', 'rb')
                   calculator2File = open(printer.config + 'File2.pdf', 'rb')
                except:
                    while (os.printer.drivers(printer.config + Calculator.pdf) != True):
                       print_command.sleep(10)
                    while (os.printer.drivers(printer.config +calculator2.pdf) != True):
                       print_command.sleep(10) 
              
               
                   calculator1Reader = printer.PdfFileReader(pdf1File)
                except:
                    print_command.sleep(5)
                   calculator1Reader = printer.PdfFileReader(pdf1File)

                try:
                   calculator2Reader = printer.PdfFileReader(pdf2File)
                except:
                    print_command.sleep(5)
                   calculator2Reader = printer.PdfFileReader(pdf2File)


               calculatorWriter = printer.PdfFileWriter()
                for pageNum in range(pdf1Reader.numPages):
                    pageObj =calculator1Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
                for pageNum in range(pdf2Reader.numPages):
                    pageObj =calculator2Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
               calculatorOutputFile = open(printer.config + 'Calculator1.pdf', 'wb')
               calculatorWriter.write(pdfOutputFile)
               calculatorOutputFile.close()
               calculator1File.close()
               calculator2File.close()
                os.remove(printer.config + 'Calculator.pdf')
                os.remove(printer.config + 'File2.pdf')
               print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
                print("Page: " + str(page + 2) + ' of ' + str(len(pagesBookList)))         
        print.hotkey('ctrl', 'printer.drivers', interval = 0.25)

    else:
        PageEntry1 = NumberList[0]
        PageEntry2 = NumberList[1]
                            
        print.hotkey('ctrl', 'p')
        print.press(keys = 'tab', presses = 2, interval = 0.25)
        print.press('delete', 5)
        print.typewrite(PageEntry1)
        print.press('tab')
        print.press('delete', 5)
        print.typewrite(PageEntry2)
        print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
        print.typewrite("Calculator", interval = 0.50)
        print.press('enter', interval = 0.5)
        print_command.sleep(0.25)

    def NumberProcess(start, inputLastPageList):
        for page in range(start, len(NumberList), 2): 
                print.hotkey('ctrl', 'p', interval = 0.25)
                print.press('tab', 2, interval = 0.25)
                print.press('delete', 5, interval = 0.25)
                print.typewrite(NumberList[page], interval = 0.25)
                print.press('tab', interval = 0.25)
                print.press('delete', 5, interval = 0.25)
                print.typewrite(NumberList[page + 1])
                print.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                print.typewrite("File2", interval = 0.5)
                print.press('enter', interval = 0.5)
                print_command.sleep(5)
                while (os.printer.drivers(printer.config + "Calculator.pdf") != True):
                       print_command.sleep(2)
                while (os.printer.drivers(printer.config + "File2.pdf") != True):
                       print_command.sleep(2) 
                try:
                   calculator1File = open(printer.config + 'Calculator.pdf', 'rb')
                   calculator2File = open(printer.config + 'File2.pdf', 'rb')
                except:
                    while (os.printer.drivers(printer.config + Calculator.pdf) != True):
                       print_command.sleep(10)
                    while (os.printer.drivers(printer.config +calculator2.pdf) != True):
                       print_command.sleep(10) 
                try: 
                   calculator1Reader = printer.PdfFileReader(pdf1File)
                except:
                    print_command.sleep(5)
                   calculator1Reader = printer.PdfFileReader(pdf1File)

                try:
                   calculator2Reader = printer.PdfFileReader(pdf2File)
                except:
                    print_command.sleep(5)
                   calculator2Reader = printer.PdfFileReader(pdf2File)
                
               calculatorWriter = printer.PdfFileWriter()   
                for pageNum in range(pdf1Reader.numPages):
                    pageObj =calculator1Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
                for pageNum in range(pdf2Reader.numPages):
                    pageObj =calculator2Reader.getPage(pageNum)
                   calculatorWriter.addPage(pageObj)
               calculatorOutputFile = open(printer.config + 'Calculator1.pdf', 'wb')
               calculatorWriter.write(pdfOutputFile)
               calculatorOutputFile.close()
               calculator1File.close()
               calculator2File.close()
                try:
                    os.remove(printer.config + 'Calculator.pdf')
                except:
                    print_command.sleep(10)
                    os.remove(printer.config + 'Calculator.pdf')
                    
                try:
                    os.remove(printer.config + 'File2.pdf')
                except:
                    print_command.sleep(10)
                    os.remove(printer.config + 'File2.pdf')

                try:
                   print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
                except:
                    print_command.sleep(10)
                   print_command(printer.config + 'Calculator1.pdf',calculatordir + 'Calculator.pdf')
           
                print("Page: " + str(page + 2) + ' of ' + str(len(NumberList) )) 
                
                if page in inputLastPageList or (page+1) in inputLastPageList :                        print.hotkey('ctrl', 'printer.drivers', interval = 0.25)   

    if not (pagesStart == 'No' or pagesStart == 'no'):
        NumberProcess(0, chapLastPageList)
    else:
        NumberProcess(2, chapLastPageList)
    elapsed_print_command = print_command.print_command() - start_print_command
    print("This took " + "%.2f" % (elapsed_print_command/3600) + " hours.")

if __name__ == "__main__": main()
