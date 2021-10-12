from tkinter import*
import tkinter.messagebox


class BMI:

    def __init__(self, root):
        self.root = root
        self.root.title("Body Mass Index")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='Gray')

    # =========================frame======================================

        MainFrme = Frame(self.root, bd=20, width=1350, height=700,
                         padx=10, pady=10, bg="Gray", relief=RIDGE)
        MainFrme.grid()

        LeftFrme = Frame(MainFrme, bd=10, width=600, height=700,
                         padx=10, pady=13, bg="Gray", relief=RIDGE)
        LeftFrme.pack(side=LEFT)

        RightFrme = Frame(MainFrme, bd=10, width=560, height=700,
                          padx=10, pady=13, relief=RIDGE)
        RightFrme.pack(side=LEFT)
    # =========================frame======================================
        LeftFrme0 = Frame(LeftFrme, bd=5, width=712, height=143,
                          padx=5, bg="blue", relief=RIDGE)
        LeftFrme0.grid(row=0, column=0)
        LeftFrme1 = Frame(LeftFrme, bd=5, width=712, height=170,
                          padx=5, pady=5, relief=RIDGE)
        LeftFrme1.grid(row=4, column=0)
        leftFrme2 = Frame(LeftFrme, bd=5, width=712, height=168,
                          padx=5, pady=6, relief=RIDGE)
        leftFrme2.grid(row=2, column=0)
        LeftFrme3 = Frame(LeftFrme, bd=5, width=712, height=95,
                          padx=5, pady=5, relief=RIDGE)
        LeftFrme3.grid(row=3, column=0)

        RightFrme0 = Frame(RightFrme, bd=5, width=522, height=200,
                           padx=5, pady=2, relief=RIDGE)
        RightFrme0.grid(row=0, column=0)
        RightFrme1 = Frame(RightFrme, bd=5, width=522, height=280,
                           padx=5, relief=RIDGE)
        RightFrme1.grid(row=1, column=0)
        rightFrme2 = Frame(RightFrme, bd=5, width=522, height=95,
                           padx=5, pady=2, bg="Gray", relief=RIDGE)
        rightFrme2.grid(row=2, column=0)
# =================================================================================
        var1 = StringVar()
        var2 = StringVar()
        var3 = DoubleVar()
        var4 = DoubleVar()
# =================================================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Body Mass Index", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def reset():
            var1.set("")
            var2.set("")
            var3.set(0)
            var4.set(0)
            self.txtBMIResult.delete("1.0", END)

        def BMI_Cal():
            BHeight = (var1.get())
            BWidth = (var2.get())
            self.txtBMIResult.delete("1.0", END)

            if(BHeight.isdigit() or BWidth.isdigit()):
                BHeight = float(BHeight)
                BWidth = float(BWidth)
                BMI = float('%.2f' % (BWidth / (BHeight * BHeight)))
                self.txtBMIResult.insert(END, BMI)
                var3.set(BHeight)
                var4.set(BWidth)
                return True
            else:
                tkinter.messagebox.showwarning(
                    "Body Mass Index", "Division by zero is invalid,Enter a valid number")
                var1.set("")
                var2.set("")
                var3.set(0)
                var4.set(0)
                self.txtBMIResult.delete("1.0", END)

# =================================================================================

        self.lblTitle = Label(
            LeftFrme0, text="Body Mass Index", padx=17, pady=4, bd=1, fg="#000000", font=('arial', 40, 'bold'), bg='blue', width=20)
        self.lblTitle.pack()

        self.BodyHeight = Scale(RightFrme0, variable=var3, from_=1, to=5, length=507, tickinterval=1,
                                orient=HORIZONTAL, label="Height in Meters Square", font=('arial', 10, 'bold'))
        self.BodyHeight.grid(row=1, column=0)

        self.BodyWidth = Scale(rightFrme2, variable=var4, from_=1, to=500, length=507, tickinterval=50,
                               orient=HORIZONTAL, label="Weight in Kilograms", font=('arial', 10, 'bold'))
        self.BodyWidth.grid(row=1, column=0)

        self.lblBMMITable = Label(RightFrme1, font=(
            'arial', 20, 'bold'), text="\tMNI Table").grid(row=0, column=0)
        self.txtBMITable = Text(RightFrme1, height=12,
                                width=53, bd=16, font=('arial', 12, 'bold'))
        self.txtBMITable.grid(row=1, column=0, columnspan=3)

        self.txtBMITable.insert(END, 'Meaning \t\t\t\t' + "BMI \n\n")
        self.txtBMITable.insert(
            END, 'Normal Weight \t\t\t\t' + "19 - 24,9 \n\n")
        self.txtBMITable.insert(END, 'Overweight \t\t\t\t' + "25-29.9 \n\n")
        self.txtBMITable.insert(
            END, 'Obesity level 1 \t\t\t\t' + "30 - 34.9 \n\n")
        self.txtBMITable.insert(
            END, 'Obesity level 11 \t\t\t\t' + "35 - 39.9 \n\n")
        self.txtBMITable.insert(
            END, 'Obesity level 111 \t\t\t\t' + "> 40 \n\n")
# =================================================================================
        self.lblHeight = Label(leftFrme2, text="Enter Height in Meters Sequare:", font=(
            'arial', 20, 'bold'), bd=2, justify=LEFT)
        self.lblHeight.grid(row=0, column=0, padx=15)
        self.txtHeight = Entry(leftFrme2, textvariable=var1, font=(
            'arial', 20, 'bold'), bd=5, width=15, justify=RIGHT)
        self.txtHeight.grid(row=0, column=1, pady=10)

        self.lblWeight = Label(leftFrme2, text="Enter Height in Kilograms:", font=(
            'arial', 20, 'bold'), bd=2, justify=LEFT)
        self.lblWeight.grid(row=1, column=0)
        self.txtWeight = Entry(leftFrme2, textvariable=var2, font=(
            'arial', 20, 'bold'), bd=5, width=15, justify=RIGHT)
        self.txtWeight.grid(row=1, column=1, pady=10)

        self.lblBMIResult = Label(LeftFrme3, text="Your BMI Result is :", font=(
            'arial', 20, 'bold'), bd=2, justify=LEFT)
        self.lblBMIResult.grid(row=0, column=0)
        self.txtBMIResult = Text(LeftFrme3, padx=105, pady=5, font=(
            'arial', 20, 'bold'), bd=5, bg="blue", relief='sunk', width=13, height=1)
        self.txtBMIResult.grid(row=0, column=1)
# =================================================================================
        self.btnBMI = Button(LeftFrme1, text="Calculate BMI", padx=4, pady=2, bd=4, width=12, font=(
            'arial', 20, 'bold'), height=4, command=BMI_Cal)
        self.btnBMI.grid(row=3, column=0)

        self.btnBMIReset = Button(LeftFrme1, text="Reset", padx=4, pady=2, bd=4, width=12, font=(
            'arial', 20, 'bold'), height=4, command=reset)
        self.btnBMIReset.grid(row=3, column=1)

        self.btnBMIExit = Button(LeftFrme1, text="Exit", padx=4, pady=2, bd=4, width=12, font=(
            'arial', 20, 'bold'), height=4, command=iExit)
        self.btnBMIExit.grid(row=3, column=2)


if __name__ == '__main__':
    root = Tk()
    application = BMI(root)
    root.mainloop()
