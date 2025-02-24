import app
import event
import GFHhg54GHGhh45GHGH
import fgGHGjjFHJghjfFG1545gGG
import item
import ui
import uiToolTip
import mouseModule
import locale
import uiCommon
import constInfo
import dbg
import math
import shop
import chat
import localeInfo
import snd
from _weakref import proxy

class GuildStorage(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.isLoaded = FALSE

	def __Initialize(self):
		self.children = []
		self.tab = 0
		self.xGuildStorageStart = 0
		self.yGuildStorageStart = 0
		self.oldtime_ = 0
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/GuildStorage.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			
			## Guildstorage
			self.GuildStorage	= {
				"slots"					: self.GetChild("GS_Slots"),
				"tab00"					: self.GetChild("GS_Tab_00"),
				"tab01"					: self.GetChild("GS_Tab_01"),
				"tab02"					: self.GetChild("GS_Tab_02"),
				"tab03"					: self.GetChild("GS_Tab_03"),
				"tab04"					: self.GetChild("GS_Tab_04"),
				"tab05"					: self.GetChild("GS_Tab_05"),
				}
			## Guildstorage END
			
			## Money
			self.MoneyBoard = {
				"btn_money"					: self.GetChild("MoneyBoard"),
				"text"					: self.GetChild("MB_Text"),
				"board"					: GuildStorageMoneyManager(),
			}
			
			## Money END
			
			## Logs
			
			self.Logs = {
			"btn_Logs" : self.GetChild("GS_LogsButton"),
			"board"		: GuildStorageLogs(),
			}
			
			## Logs END
			
			## Adminpanel 
			self.Adminpanel = {
				"btn_Admin" : self.GetChild("GS_AdministrationButton"),
				"board"		: GuildStorageAdmin(),
			}
			## Adminpanel END
			
			##ItemToolTip
			self.toolTip = uiToolTip.ItemToolTip()
			##ItemToolTip END
		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		
		for i in range(6):
			self.GuildStorage["tab0"+str(i)].SetEvent(self.ChangeTab,i)
			
		
		self.toolTip = uiToolTip.ItemToolTip()
		self.GuildStorage["slots"].SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.GuildStorage["slots"].SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.GuildStorage["slots"].SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.GuildStorage["slots"].SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.GuildStorage["slots"].SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemSlot))
		self.GuildStorage["slots"].SetUsableItem(True)
		
		self.MoneyBoard["btn_money"].SetEvent(self.ShowMoneyManager)
		
		self.Adminpanel["btn_Admin"].SetEvent(self.ShowAdminPanel)
		self.Logs["btn_Logs"].SetEvent(self.ShowLogs)
		
		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		
	def Open(self,mode):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.__Initialize()
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Du kannst das Gildenlager nicht oeffnen, solange du ein Item droppst.")
			self.Close()
			return
		if mouseModule.mouseController.isAttached():
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Du kannst das Gildenlager nicht oeffnen, solange du ein Item haelst.")
			self.Close()
			return
		constInfo.GUILDSTORAGE["open"] = 1
		
		self.StandartInterface()
		
		## clear the slots
		for i in range(120):
			self.GuildStorage["slots"].ClearSlot(i)
			
		if mode == 0:
			self.Adminpanel["btn_Admin"].Hide()
			self.Logs["btn_Logs"].Hide()
		else:
			self.Adminpanel["btn_Admin"].Show()
			self.Logs["btn_Logs"].Show()
			
		(self.xGuildStorageStart, self.yGuildStorageStart, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		self.SetTop()
		self.Show()
		
	def StandartInterface(self):
		self.GuildStorage["tab00"].Down()
		self.GuildStorage["tab01"].SetUp()
		self.GuildStorage["tab02"].SetUp()
		self.GuildStorage["tab03"].SetUp()
		self.GuildStorage["tab04"].SetUp()
		self.GuildStorage["tab05"].SetUp()
		constInfo.GUILDSTORAGE["slots"] = {"TAB0" : {},"TAB1" : {},"TAB2" : {},"TAB3" : {},"TAB4" : {},"TAB5" : {}}
		constInfo.GUILDSTORAGE["members"] = {}
		self.tab = 0
			
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<System>: "+str(text))
		
	def ChangeTab(self, tab):
		self.tab = tab
		for i in range(6):
			if i != tab:
				self.GuildStorage["tab0"+str(i)].SetUp()
		self.RefreshSlots()
		
	def AddItemSlot(self, slot, tab ,itemVnum, count, socket0, socket1, socket2, socket3, socket4, socket5, attrtype0,attrvalue0, attrtype1,attrvalue1, attrtype2, attrvalue2, attrtype3, attrvalue3, attrtype4, attrvalue4, attrtype5, attrvalue5, attrtype6, attrvalue6):
		constInfo.GUILDSTORAGE["slots"]["TAB"+tab][int(slot)] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		self.RefreshSlots()
		
	def MoveItemSlot(self,from_,to_):
		item = constInfo.GUILDSTORAGE["slots"]["TAB"+str(from_[0])][from_[1]]
		constInfo.GUILDSTORAGE["slots"]["TAB"+str(from_[0])].pop(from_[1],None)
		constInfo.GUILDSTORAGE["slots"]["TAB"+str(to_[0])][to_[1]] = item
		self.RefreshSlots()
					
	def RefreshSlots(self):
		items = constInfo.GUILDSTORAGE["slots"]["TAB"+str(self.tab)]
		for i in range(121):
			self.GuildStorage["slots"].ClearSlot(i)
		for i in items:
			self.GuildStorage["slots"].SetItemSlot(i, items[i][0], items[i][1])
		
		self.GuildStorage["slots"].RefreshSlot()
		
	######################
	## MoneyManager START
	######################
		
	def SetMoney(self,money):
		self.MoneyBoard["text"].SetText(localeInfo.NumberToMoneyString(money))

	def ShowMoneyManager(self):
		self.MoneyBoard["board"].Open()

	# unused
	def HideMoneyManager(self):
		self.MoneyBoard["board"].Close()
		
	def GetMoneyManager(self):
		return self.MoneyBoard["board"]
	# unused END

	######################
	## MoneyManager END
	######################
		
	######################
	## Item Tool Tip START
	######################
		
	def OverInItem(self, index):
		items = constInfo.GUILDSTORAGE["slots"]["TAB"+str(self.tab)]
		self.toolTip.ClearToolTip()
		self.toolTip.AddRefineItemData(items[index][0], [items[index][2],items[index][3],items[index][4],items[index][5],items[index][6],items[index][7]],  [(items[index][8],items[index][9]),(items[index][10],items[index][11]),(items[index][12],items[index][13]),(items[index][14],items[index][15]),(items[index][16],items[index][17]),(items[index][18],items[index][19]),(items[index][20],items[index][21])])
		
		
	def OverOutItem(self):
		self.toolTip.Hide()
		
	######################
	## Item Tool Tip END
	######################
		
	######################
	## Storage Drag START
	######################
	
	def SelectEmptySlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			
			if constInfo.BlockItemsSystem["Block"] == 1:
				chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
				return
			
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.QuestCMD("MOVE_ITEM#INVENTORY#"+str(attachedSlotPos)+"#"+str(selectedSlotPos)+"#"+str(self.tab))
			elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY != attachedSlotType and fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_MALL != attachedSlotType and fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SAFEBOX != attachedSlotType and fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SHOP != attachedSlotType:
				self.QuestCMD("MOVE_ITEM#GUILDSTORAGE#"+str(attachedSlotPos)+"#"+str(self.temporaryTab)+"#"+str(selectedSlotPos)+"#"+str(self.tab))
				self.MoveItemSlot([self.temporaryTab,attachedSlotPos],[self.tab,selectedSlotPos])

		mouseModule.mouseController.DeattachObject()

	def UnselectItemSlot(self, selectedSlotPos):
		self.QuestCMD("TAKE_ITEM#"+str(selectedSlotPos)+"#"+str(self.tab))
		constInfo.GUILDSTORAGE["slots"]["TAB"+str(self.tab)].pop(selectedSlotPos,None)
		self.RefreshSlots()
		

	def SelectItemSlot(self, selectedSlotPos):
		items = constInfo.GUILDSTORAGE["slots"]["TAB"+str(self.tab)]
		curCursorNum = app.GetCursor()
		selectedSlotPos = selectedSlotPos
		selectedItemID = items[selectedSlotPos][0]
		itemCount = items[selectedSlotPos][1]

		type = fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_PRIVATE_SHOP
		mouseModule.mouseController.AttachObject(self, type, selectedSlotPos, selectedItemID, itemCount)
		self.temporaryTab = self.tab
		mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
		snd.PlaySound("sound/ui/pick.wav")
		
		
	def DropToInventory(self):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.QuestCMD("TAKE_ITEM#"+str(attachedSlotPos)+"#"+str(self.tab))
		constInfo.GUILDSTORAGE["slots"]["TAB"+str(self.tab)].pop(attachedSlotPos,None)
		self.RefreshSlots()
			
	######################
	## Storage Drag END
	######################
	
	def QuestCMD(self, command):
		constInfo.GUILDSTORAGE["questCMD"] = command
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		
	def ShowAdminPanel(self):
		self.Adminpanel['board'].Open()
		
	def LogsInsert(self,id,name,date,type,do,desc):
		self.Logs['board'].LogsInsert(id,name,date,type,do,desc)
		
	def ShowLogs(self):
		self.Logs['board'].Open()
		
	def OnUpdate(self):
		USE_GUILDSTORAGE_LIMIT_RANGE = 1000

		(x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		if abs(x - self.xGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE or abs(y - self.yGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE:
			self.Close()
			
		oldtime = self.oldtime_
		newtime = app.GetTime()
		newcalc = newtime - oldtime
		intnewcalc = int(newcalc)
		if newcalc > 5:
			self.oldtime_ = newtime
			self.QuestCMD("UPDATE#")
		
	def Close(self):
		constInfo.GUILDSTORAGE["open"] = 0
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
	def ClearMembers(self):
		self.Adminpanel['board'].ClearMembers()
		

class MouseReflector(ui.Window):
	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.AddFlag("not_pick")
		self.width = self.height = 0
		self.isDown = FALSE

	def Down(self):
		self.isDown = TRUE

	def Up(self):
		self.isDown = FALSE

	def OnRender(self):
		import grp
		if self.isDown:
			grp.SetColor(ui.WHITE_COLOR)
		else:
			grp.SetColor(ui.HALF_WHITE_COLOR)

		x, y = self.GetGlobalPosition()
		grp.RenderBar(x+2, y+2, self.GetWidth()-4, self.GetHeight()-4)

class CheckBox(ui.ImageBox):
	def __init__(self, parent, x, y, event, filename = "d:/ymir work/ui/public/Parameter_Slot_01.sub"):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage(filename)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = TRUE
		self.Checked = FALSE
		self.image = image
		self.event = event
		self.Show()

		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
			self.Checked = TRUE
		else:
			self.image.Hide()
			self.Checked = FALSE
		
	def GetCheck(self):
		return self.Checked

	def Disable(self):
		self.Enable = FALSE

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event()
		
		

class GuildStorageAdmin(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.isLoaded = FALSE

	def __Initialize(self):
		self.children = []
		self.xGuildStorageStart = 0
		self.yGuildStorageStart = 0
		self.startpos = 0
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/GuildStorageAdmin.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			self.AddMemberButton = self.GetChild("GS_AddMember")
			self.MemberInput = self.GetChild("GS_MemberInputLine")
			self.scrollbar = self.GetChild("scrollbar")
			
			self.scrollbar.SetScrollEvent(ui.__mem_func__(self.__OnScroll))
			
			self.MemberPage = {
			}
			
			for i in range(12):
				event = lambda argSelf=proxy(self), argIndex=i, argAuthority=0: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
				self.MemberPage['stock'+str(i)] = (CheckBox(self.board, 130, 60+(20*i), event))
				
				event = lambda argSelf=proxy(self), argIndex=i, argAuthority=1: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
				self.MemberPage['transfer'+str(i)] = (CheckBox(self.board, 190, 60+(20*i), event))
				
				event = lambda argSelf=proxy(self), argIndex=i, argAuthority=2: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
				self.MemberPage['payin'+str(i)] = (CheckBox(self.board, 250, 60+(20*i), event))
				
				event = lambda argSelf=proxy(self), argIndex=i, argAuthority=3: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
				self.MemberPage['payout'+str(i)] = (CheckBox(self.board, 310, 60+(20*i), event))
				
				self.MemberPage['membername_slotbar'+str(i)] = ui.MakeSlotBar(self.board, 20, 61+(20*i), 100,16)
				self.MemberPage['membername_text'+str(i)] = ui.MakeTextLine(self.MemberPage['membername_slotbar'+str(i)])

				self.MemberPage['deleteBTN'+str(i)] = ui.MakeButton(self.board, 365, 61+(20*i), "loeschen", "d:/ymir work/ui/public/", "close_button_01.sub", "close_button_02.sub", "close_button_03.sub")
				self.MemberPage['deleteBTN'+str(i)].SetEvent(ui.__mem_func__(self.DeleteMember), i)

		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		self.AddMemberButton.SetEvent(self.AddMember)
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.isLoaded = TRUE
				
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Close()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.__Initialize()
		self.QuestCMD("GETMEMBERLIST")
		self.SetTop()
		self.Show()
		self.scrollbar.SetPos(0)
		(self.xGuildStorageStart, self.yGuildStorageStart, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		self.MemberInput.SetText("Membername")
		
	def OnUpdate(self):
		USE_GUILDSTORAGE_LIMIT_RANGE = 1000

		(x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		if abs(x - self.xGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE or abs(y - self.yGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE:
			self.Close()
			
	######################
	## Gui elements START
	######################
	
	def __OnScroll(self):
		members = constInfo.GUILDSTORAGE["members"]
		memberslen = len(members)##itemlen
		self.startpos = int(self.scrollbar.GetPos() * (memberslen-12))
		
		# self.SendSystemChat(str(self.startpos))
		
		if memberslen > 12:
			self.RefreshMembers(self.startpos)

	def Create_SlotLine(self, parent, editlineText, x, y, width, heigh):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		textline = ui.TextLine()
		textline.SetParent(SlotBar)
		textline.SetPosition(2, 2)
		textline.SetText(editlineText)
		textline.Show()
		return textline
		
	######################
	## Gui elements STOP
	######################
	
	
	######################
	## Admininstration Panel START
	######################
	
	def AddMember(self):
		membername = self.MemberInput.GetText()
		
		if membername == "":
			self.SendSystemChat("Du musst einen Membernamen eingeben")
			return
			
		for i in xrange(len(membername)):
			if membername[i] == "!" or membername[i] == "%":
				self.SendSystemChat("Dieser Name besitzt ung�ltige zeichen!")
				return				
		
		self.QuestCMD("ADD_MEMBER#"+str(membername))
		self.MemberInput.SetText("Membername")
		
	def RefreshMembers(self,pos):
		members = constInfo.GUILDSTORAGE["members"]
		if len(members) <= 12:## Set scrollbar middle Size, show or hide
			
			self.scrollbar.Hide()
		else:
			self.scrollbar.SetMiddleBarSize(float(12)/float(len(members)))
			self.scrollbar.Show()
		for i in range(12):
			try:
				index = i + pos
				member = members["member"+str(index)]
				self.MemberPage['membername_text'+str(i)].SetText(member[0])
				
				if member[1] == 0:
					self.MemberPage['stock'+str(i)].SetCheck(FALSE)
				else:
					self.MemberPage['stock'+str(i)].SetCheck(TRUE)
				if member[2] == 0:
					self.MemberPage['transfer'+str(i)].SetCheck(FALSE)
				else:
					self.MemberPage['transfer'+str(i)].SetCheck(TRUE)
				if member[3] == 0:
					self.MemberPage['payin'+str(i)].SetCheck(FALSE)
				else:
					self.MemberPage['payin'+str(i)].SetCheck(TRUE)
				if member[4] == 0:
					self.MemberPage['payout'+str(i)].SetCheck(FALSE)
				else:
					self.MemberPage['payout'+str(i)].SetCheck(TRUE)
			except:
				return
				
	def ClearMembers(self):
		members = constInfo.GUILDSTORAGE["members"]
		self.scrollbar.SetPos(0)
		for i in range(12):
			self.MemberPage['membername_text'+str(i)].SetText('')
			self.MemberPage['stock'+str(i)].SetCheck(FALSE)
			self.MemberPage['transfer'+str(i)].SetCheck(FALSE)
			self.MemberPage['payin'+str(i)].SetCheck(FALSE)
			self.MemberPage['payout'+str(i)].SetCheck(FALSE)
		
	def DeleteMember(self, btID):
		memberName = self.MemberPage['membername_text'+str(btID)].GetText()
		if memberName == "":
			return
		self.QuestCMD("DELETE_MEMBER#"+memberName)
	
	def OnCheckAuthority(self, argIndex, argAuthority):
		memberName = self.MemberPage['membername_text'+str(argIndex)].GetText()
		if memberName == "":
			return
		authority = FALSE
		if argAuthority == 0:
			if self.MemberPage['stock'+str(argIndex)].GetCheck():
				self.MemberPage['stock'+str(argIndex)].SetCheck(FALSE)
			else:
				self.MemberPage['stock'+str(argIndex)].SetCheck(TRUE)
				authority = TRUE
		elif argAuthority == 1:
			if self.MemberPage['transfer'+str(argIndex)].GetCheck():
				self.MemberPage['transfer'+str(argIndex)].SetCheck(FALSE)
			else:
				self.MemberPage['transfer'+str(argIndex)].SetCheck(TRUE)
				authority = TRUE
		elif argAuthority == 2:
			if self.MemberPage['payin'+str(argIndex)].GetCheck():
				self.MemberPage['payin'+str(argIndex)].SetCheck(FALSE)
			else:
				self.MemberPage['payin'+str(argIndex)].SetCheck(TRUE)
				authority = TRUE
		elif argAuthority == 3:
			if self.MemberPage['payout'+str(argIndex)].GetCheck():
				self.MemberPage['payout'+str(argIndex)].SetCheck(FALSE)
			else:
				self.MemberPage['payout'+str(argIndex)].SetCheck(TRUE)
				authority = TRUE
				
		self.QuestCMD("AUTHORITY#"+memberName+"#"+str(argAuthority)+"#"+str(authority))

	######################
	## Admininstration Panel END
	######################
	
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<System>: "+str(text))
		
	def QuestCMD(self, command):
		constInfo.GUILDSTORAGE["questCMD"] = command
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		

class GuildStorageLogs(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.isLoaded = FALSE

	def __Initialize(self):
		self.children = []
		self.xGuildStorageStart = 0
		self.yGuildStorageStart = 0
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/GuildStorageLogs.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			
			self.Logs = self.GetChild("LM_LogsGroupBox")
			
			self.Search = {
			"btn" : self.GetChild("LS_Search"),
			"text" : self.GetChild("LS_SearchInputLine"),
			}
			
			self.DeleteBtn = self.GetChild("LM_Delete")

		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.Logs.SetTextCenterAlign(FALSE)
		
		self.DeleteBtn.SetEvent(self.DeleteLogs)
		self.Search['btn'].SetEvent(self.SearchMember)

		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def LogsInsert(self,id,name,date,type,do,desc):
		self.Logs.InsertItem(id, '[Member]: '+name+'\t'+'[Datum]: '+date+'\t'+'[Art]: '+type+'\t'+'[Taetigkeit]: '+do+'\t'+'-> '+desc)
		
	def SearchMember(self):
		name = self.Search['text'].GetText()
		if name == "":
			self.Refresh()
		else:
			self.Logs.ClearItem()
			log = constInfo.GUILDSTORAGE["logs"]
			for i in range(len(log)):
				# self.SendSystemChat('LOG'+log[i][0])
				if log[i][0].find(name) != -1:
					self.LogsInsert(i,log[i][0],log[i][1],log[i][2],log[i][3],log[i][4])
			
	def Refresh(self):
		self.Logs.ClearItem()
		log = constInfo.GUILDSTORAGE["logs"]
		for i in range(len(log)):
			self.LogsInsert(i,log[i][0],log[i][1],log[i][2],log[i][3],log[i][4])
			
	def DeleteLogs(self):
		self.Logs.ClearItem()
		constInfo.GUILDSTORAGE["logs"] = {}
		self.QuestCMD("DELETE_LOGS#")

	def Destroy(self):
		self.Close()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.__Initialize()
		self.SetTop()
		self.Show()
		(self.xGuildStorageStart, self.yGuildStorageStart, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		constInfo.GUILDSTORAGE["logs"] = {}
		self.Logs.ClearItem()
		self.QuestCMD("LOAD_LOGS#")
		
	def OnUpdate(self):

		USE_GUILDSTORAGE_LIMIT_RANGE = 1000

		(x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		if abs(x - self.xGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE or abs(y - self.yGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE:
			self.Close()
	
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<System>: "+str(text))
		
	def QuestCMD(self, command):
		constInfo.GUILDSTORAGE["questCMD"] = command
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		

class GuildStorageMoneyManager(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.isLoaded = FALSE

	def __Initialize(self):
		self.children = []
		self.xGuildStorageStart = 0
		self.yGuildStorageStart = 0
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/GuildStorageMoneyManager.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			self.GetChild("CashInButton").SetEvent(self.CashInButton)
			self.GetChild("CashOutButton").SetEvent(self.CashOutButton)
			self.amountInput = self.GetChild("AmountInput")

		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		self.amountInput.SetNumberMode()
			
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.isLoaded = TRUE
			

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		

	def Destroy(self):
		self.Close()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.__Initialize()
		self.SetTop()
		self.Show()
		(self.xGuildStorageStart, self.yGuildStorageStart, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		self.amountInput.SetText("1")
		
	def OnUpdate(self):

		USE_GUILDSTORAGE_LIMIT_RANGE = 1000

		(x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		if abs(x - self.xGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE or abs(y - self.yGuildStorageStart) > USE_GUILDSTORAGE_LIMIT_RANGE:
			self.Close()
		
	def CashOutButton(self):
		money = self.amountInput.GetText()
		if money == "":
			self.amountInput.SetText("1")
			return
		self.QuestCMD("TAKE_MONEY#"+str(money))
		self.amountInput.SetText("1")
		self.Close()
	
	def CashInButton(self):
		money = self.amountInput.GetText()
		if money == "":
			self.amountInput.SetText("1")
			return
		self.QuestCMD("GIVE_MONEY#"+str(money))
		self.amountInput.SetText("1")
		self.Close()
	
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<System>: "+str(text))
		
	def QuestCMD(self, command):
		constInfo.GUILDSTORAGE["questCMD"] = command
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
