import tkinter as tk
from tkinter import ttk
from tkinter.constants import ACTIVE
import random

#main
class win1(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack()
		self.master.title("High & Low game")
		self.master.geometry("400x600")
		self.value1 = 0
		self.value2 = 0
		self.count = 0
		self.max_count = 0

		#説明文
		label = tk.Label(text = "ハイアンドローゲーム\nコンピューターが選ぶ数字１～１３が\n次に選ぶ値より大きいか小さいかを選びます")
		label.pack()
		#cpu1で上書き
		self.cpu_txt = tk.Label(text = "")
		self.cpu_txt.pack(pady = 30)
		self.cpu1_txt = tk.Label(text = "")
		self.cpu1_txt.place(x = 30, y = 150)
		self.cpu1_txt1 = tk.Label(text = "")
		self.cpu1_txt1.place(x = 199, y = 150)
		#cpu2で上書き
		self.cpu2_txt = tk.Label(text = "")
		self.cpu2_txt.place(x = 30, y = 200)
		self.cpu2_txt1 = tk.Label(text = "")
		self.cpu2_txt1.place(x = 199, y = 200)
		#結果
		self.txt = ttk.Label(text = "")
		self.txt.pack(pady = 100)
		#スタートボタン
		self.strt_bt = ttk.Button()
		self.strt_bt.configure(text = "START")
		self.strt_bt.configure(default = ACTIVE)
		self.strt_bt.configure(command = self.cpu1)
		self.strt_bt.pack(pady = 100)
		#highボタン
		self.high_bt = ttk.Button()
		self.high_bt.configure(text = "HIGH")
		self.high_bt.configure(command = self.cpuh)
		self.high_bt.place_forget()
		#lowボタン
		self.low_bt = ttk.Button()
		self.low_bt.configure(text = "LOW")
		self.low_bt.configure(command = self.cpul)
		self.low_bt.place_forget()
		#continueボタン
		self.con_bt = ttk.Button()
		self.con_bt.configure(text = "continue")
		self.con_bt.configure(command = self.cpu1)
		self.con_bt.place_forget()
		#foldボタン
		self.fol_bt = ttk.Button()
		self.fol_bt.configure(text = "fold")
		self.fol_bt.configure(command = self.kekka)
		self.fol_bt.place_forget()
		#endボタン
		self.end_bt = ttk.Button()
		self.end_bt.configure(text = "End")
		self.end_bt.configure(command = self.quit)
		self.end_bt.pack_forget()

	#スタートボタンとコンテニューボタン
	def cpu1(self):
		self.value1 = random.randint(1,13)
		self.cpu_txt["text"] = "コンピュータが選択した数字"
		self.cpu1_txt["text"] = "１回目："
		self.cpu1_txt1["text"] = str(self.value1)
		self.high_bt.place(x = 100, y = 300)
		self.low_bt.place(x = 200, y = 300)
		self.strt_bt.pack_forget()
		self.con_bt.place_forget()
		self.fol_bt.place_forget()
		self.cpu2_txt["text"] = ""
		self.cpu2_txt1["text"] = ""
		self.txt["text"] = "Current Wins：" + str(self.count)
		

	#highボタンとlowボタン
	def cpu2(self):
		self.value2 = random.randint(1,13)
		self.cpu2_txt["text"] = "２回目："
		self.cpu2_txt1["text"] = str(self.value2)
		self.con_bt.place(x = 100, y = 300)
		self.fol_bt.place(x = 200, y = 300)
		self.high_bt.place_forget()
		self.low_bt.place_forget()
		

	def cpuh(self):
		self.cpu2()

		if self.value1 > self.value2:
			self.count += 1
			self.txt["text"] = "rigth\nCurrent Wins：" + str(self.count)
			if self.max_count < self.count:
				self.max_count = self.count
		elif self.value1 == self.value2:
			self.txt["text"] = "Even\nCurrent Wins：" + str(self.count)
		else:
			self.count = 0
			self.txt["text"] = "wrong"

	def cpul(self):
		self.cpu2()

		if self.value1 < self.value2:
			self.count += 1
			self.txt["text"] = "rigth\nCurrent Wins：" + str(self.count)
			if self.max_count < self.count:
				self.max_count = self.count
		elif self.value1 == self.value2:
			self.txt["text"] = "Even\nCurrent Wins：" + str(self.count)
		else:
			self.count = 0
			self.txt["text"] = "wrong"
	
	def kekka(self):
		self.con_bt.place_forget()
		self.fol_bt.place_forget()
		self.txt["text"] = ""

		global max_count

		kekka = ttk.Label(text = "あなたの最高連続勝利数：　" + str(self.max_count))
		kekka.pack(pady = 50)
		self.end_bt.pack()

	def quit(self):
		self.master.destroy()

def main():
    root = tk.Tk()
    app = win1(master = root)
    app.mainloop()

if __name__ == "__main__":
    main()