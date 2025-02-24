import ui
import GFHhg54GHGhh45GHGH
import item
import skill
import localeInfo
import wndMgr
import fgGHGjjFHJghjfFG1545gGG
import constInfo
import mouseModule
import uiScriptLocale
import app
import playerSettingModule
import uiToolTip
import settinginfo
import exterminatus
import background
import chat
import systemSetting

MOUSE_SETTINGS = [0, 0]

def InitMouseButtonSettings(left, right):
	global MOUSE_SETTINGS
	MOUSE_SETTINGS = [left, right]

def SetMouseButtonSetting(dir, event):
	global MOUSE_SETTINGS
	MOUSE_SETTINGS[dir] = event
	
def GetMouseButtonSettings():
	global MOUSE_SETTINGS
	return MOUSE_SETTINGS

def SaveMouseButtonSettings():
	global MOUSE_SETTINGS
	open("mouse.cfg", "w").write("%s\t%s" % tuple(MOUSE_SETTINGS))

def LoadMouseButtonSettings():
	global MOUSE_SETTINGS
	tokens = open("mouse.cfg", "r").read().split()

	if len(tokens) != 2:
		raise RuntimeError, "MOUSE_SETTINGS_FILE_ERROR"

	MOUSE_SETTINGS[0] = int(tokens[0])
	MOUSE_SETTINGS[1] = int(tokens[1])

def unsigned32(n):
	return n & 0xFFFFFFFFL

	
class ButtonToolTipWindow(ui.Window):
	BUTTON_CHARACTER = 0
	BUTTON_INVENTORY = 1
	BUTTON_MESSENGER = 2
	BUTTON_SYSTEM = 3
	BUTTON_WARP = 5
	BUTTON_BONUS = 6
	BUTTON_EVENT = 7
	BUTTON_FORGE = 8
	BUTTON_HOF = 9	
	BUTTON_QUEST = 10
	normalWidth = 190
	
	buttonDesc = {
		BUTTON_CHARACTER : localeInfo.TASKBAR_BUTTON_DESC_CHARACTER,
		BUTTON_INVENTORY : localeInfo.TASKBAR_BUTTON_DESC_INVENTORY,
		BUTTON_MESSENGER : localeInfo.TASKBAR_BUTTON_DESC_MESSENGER,
		BUTTON_SYSTEM : localeInfo.TASKBAR_BUTTON_DESC_SYSTEM,
		BUTTON_WARP : localeInfo.TASKBAR_BUTTON_DESC_WARP,
		BUTTON_BONUS : localeInfo.TASKBAR_BUTTON_DESC_BONUS,
		BUTTON_EVENT : localeInfo.TASKBAR_BUTTON_DESC_EVENT,
		BUTTON_FORGE : localeInfo.TASKBAR_BUTTON_DESC_FORGE,
		BUTTON_HOF : localeInfo.TASKBAR_BUTTON_DESC_HOF,
		BUTTON_QUEST : localeInfo.TASKBAR_BUTTON_DESC_QUEST,
	}
	
	def __init__(self):
		ui.Window.__init__(self)
		self.titleTextLine = None
		self.descTextLine = None
		self.thinBoard = None
		self.buttonIcon = None
		self.SetSize(self.normalWidth,100)
		self.SetPosition(5,wndMgr.GetScreenHeight() - 250)
		self.Hide()
		self.MakeToolTip()	
		
	def __del__(self):
		ui.Window.__del__(self)
		
		
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(1, 1)
		toolTip.SetFollow(False)
		toolTip.Show()
		self.toolTip = toolTip
	
	def Open(self,button):
		self.toolTip.ClearToolTip()
		# self.toolTip.SetTitle("Hallo Welt!")
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendDescription(self.buttonDesc[button],26)
		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()	
		self.SetPosition(5,(wndMgr.GetScreenHeight() - 100)-self.toolTip.toolTipHeight)
		self.Show()
		
	def AppendCurrencyInfo(self,text,cur):
		self.toolTip.AppendStatisticTextLine(text,cur)
		self.toolTip.ResizeToolTip()	
		self.SetPosition(5,(wndMgr.GetScreenHeight() - 100)-self.toolTip.toolTipHeight)
	
	
	def AppendSpaceLine(self):
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.ResizeToolTip()	
		self.SetPosition(5,(wndMgr.GetScreenHeight() - 100)-self.toolTip.toolTipHeight)		
		
		
	def Close(self):
		self.Hide()
	
class PlayerFrame(ui.ScriptWindow):
	FACE_IMAGE_DICT = {
		playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
		playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
		playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
		playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
		playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
		playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
		playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
		playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
	}

	GAUGE_HP_WIDTH = 114
	GAUGE_HP_HEIGHT = 11

	GAUGE_MP_WIDTH = 105
	GAUGE_MP_HEIGHT = 11
	
	GAUGE_EXP_WIDTH = 95
	GAUGE_EXP_HEIGHT = 13
	
	TIME_GAME_START = app.GetTime()
	GOLD_GAME_START = -1
	GOLD_EARNED = 0
	
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")
			self.SetWindowName("PlayerFrame")
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)
			
	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.tooltipGift = self.TextToolTip()
		self.tooltipGift.Show()
		
	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/yplayerframe.py")
		except:
			import exception
			exception.Abort("PlayerFrame.LoadWindow.LoadObject")		

		self.playerFrameBoard = self.GetChild("PlayerFrameBase")
		self.playerFrameIcon = self.GetChild("PlayerFrameIcon")
		self.toolTipTriggerWindow = self.GetChild("statisticTriggerWindow")
		self.playerHPRecoveryBar	= self.GetChild("HPRecoveryGaugeBar")
		self.playerHPGaugeBar		= self.GetChild("HPGauge")
		#self.playerHPWindow			= self.GetChild("TPToolTipWindow")
		self.playerHPTextLine		= self.GetChild("HPInfoTextLine")
		
		self.playerMPRecoveryBar	= self.GetChild("MPRecoveryGaugeBar")
		self.playerMPGaugeBar		= self.GetChild("MPGauge")		
		#self.playerMPWindow			= self.GetChild("MPToolTipWindow")
		self.playerMPTextLine		= self.GetChild("MPInfoTextLine")
		
		self.playerLevelTextLine	= self.GetChild("PlayerLevel")
		self.playerEXPGaugeBar		= self.GetChild("EXPGauge")	
		
		self.playerEXPWindow		= self.GetChild("EXPWindow")
		self.playerEXPTextLine		= self.GetChild("EXPInfoTextLine")
		
		self.SetPlayerFrameIcon()
		
		self.playerStatisticToolTip = uiToolTip.ToolTip()
		self.playerStatisticToolTip.HideToolTip()

	def SetPlayerFrameIcon(self):
		race = GFHhg54GHGhh45GHGH.GetMainActorRace()
		self.playerFrameIcon.LoadImage(self.FACE_IMAGE_DICT[race])
		
		
		
	def SetHP(self, curPoint, recoveryPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.playerHPGaugeBar.SetPercentage(curPoint, maxPoint)
			self.playerHPTextLine.SetText("%.2f%%" % (float(curPoint) / max(1, float(maxPoint)) * 100))

			if 0 == recoveryPoint:
				self.playerHPRecoveryBar.Hide()
			else:
				destPoint = min(maxPoint, curPoint + recoveryPoint)
				newWidth = int(self.GAUGE_HP_WIDTH * (float(destPoint) / float(maxPoint)))
				self.playerHPRecoveryBar.SetSize(newWidth, self.GAUGE_HP_HEIGHT)
				self.playerHPRecoveryBar.Show()

	def SetMP(self, curPoint, recoveryPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.playerMPGaugeBar.SetPercentage(curPoint, maxPoint)
			self.playerMPTextLine.SetText("%.2f%%" % (float(curPoint) / max(1, float(maxPoint)) * 100))
			if 0 == recoveryPoint:
				self.playerMPRecoveryBar.Hide()
			else:
				destPoint = min(maxPoint, curPoint + recoveryPoint)
				newWidth = int(self.GAUGE_MP_WIDTH * (float(destPoint) / float(maxPoint)))
				self.playerMPRecoveryBar.SetSize(newWidth, self.GAUGE_MP_HEIGHT)
				self.playerMPRecoveryBar.Show()

	def SetEXP(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.playerEXPGaugeBar.SetPercentage(curPoint, maxPoint)
		
		
		
		self.playerEXPTextLine.SetText("Erfahrung: %.2f%%" % (float(curPoint) / max(1, float(maxPoint)) * 100))
		
		self.LAST_GOLD_CHECK = fgGHGjjFHJghjfFG1545gGG.GetElk()
	
	def OnMoveWindow(self, x, y):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Move!")
		systemSetting.SetPlayerFrameX(x)
		systemSetting.SetPlayerFrameY(y)
	
	def OnUpdate(self):
		self.playerLevelTextLine.SetText(str(fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)))
		
		if self.playerEXPWindow.IsIn():
			self.playerEXPTextLine.Show()
		else:
			self.playerEXPTextLine.Hide()
		
		
		if self.toolTipTriggerWindow.IsIn():
			self.playerStatisticToolTip.ClearToolTip()
			self.playerStatisticToolTip.AppendTextLine(localeInfo.PLAYER_STATISTIC_TITLE_ABOUT,self.playerStatisticToolTip.TITLE_COLOR)
			self.playerStatisticToolTip.AppendHorizontalLine()
			self.AppendPlayTime()
			self.playerStatisticToolTip.AppendSpace(5)
			self.playerStatisticToolTip.AppendHorizontalLine()
			self.playerStatisticToolTip.AppendTextLine(localeInfo.PLAYER_STATISTIC_TITLE_SESSION,self.playerStatisticToolTip.TITLE_COLOR)
			self.AppendSessionTimer()
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_GOLD,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.GOLD_EARNED]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_AP,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.AP_EARNED]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_METIN,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.STONE_KILL_TEMP]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_MONSTER,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.MONSTER_KILL_TEMP]))
			# self.playerStatisticToolTip.AppendStatisticTextLine("Dungeons abgeschlossen:",settinginfo.DUNGEON_COMPLETE_TEMP)
			self.playerStatisticToolTip.AppendSpace(5)
			self.playerStatisticToolTip.AppendHorizontalLine()
			self.playerStatisticToolTip.AppendTextLine(localeInfo.PLAYER_STATISTIC_TITLE_PVP,self.playerStatisticToolTip.TITLE_COLOR)	
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUELL_COMP,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVP_DUELL]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUELL_WON,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVP_DUELL_WON]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUELL_LOST,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVP_DUELL_LOST]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUELL_SHINSOO_KILL,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVP_SHINSOO_KILL]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUELL_CHUNJO_KILL,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVP_CHUNJO_KILL]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUELL_JINNO_KILL,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVP_JINNO_KILL]))
			self.playerStatisticToolTip.AppendSpace(5)
			self.playerStatisticToolTip.AppendHorizontalLine()
			self.playerStatisticToolTip.AppendTextLine(localeInfo.PLAYER_STATISTIC_TITLE_PVM,self.playerStatisticToolTip.TITLE_COLOR)	
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_MONSTER_COMP,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVM_MONSTER_KILL]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_METIN_COMP,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVM_STONE_KILL]))
			self.playerStatisticToolTip.AppendStatisticTextLine("Tode:",constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PLAYER_DEAD_STAT]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_DUNGEON_COMP,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVM_DUNGEON_COMPL]))
			self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_ACHIEVEMENTS_COMP,constInfo.NumberToPointString(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PVM_ACHIEVEMENT]))
			self.playerStatisticToolTip.AppendSpace(5)
			self.playerStatisticToolTip.AppendHorizontalLine()
			# self.toolTip.ResizeToolqTipText(50,20)
			self.playerStatisticToolTip.ShowToolTip()		
		else:
			self.playerStatisticToolTip.HideToolTip()
	
	def Destroy(self):		
		self.playerFrameBoard = 0
	
	
	def AppendSessionTimer(self):
		timeGone = app.GetTime() - self.TIME_GAME_START
		self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_SESSION_TIME,self.FormatTime(timeGone))
	
	def AppendPlayTime(self):
		timeGone = app.GetTime() - self.TIME_GAME_START
		sec = int(settinginfo.PLAYER_STATISTIC_DICT[settinginfo.PLAYER_PLAYTIME] * 60) + timeGone
		self.playerStatisticToolTip.AppendStatisticTextLine(localeInfo.PLAYER_STATISTIC_PLAYTIME,localeInfo.SecondToDHM(sec))
	# def CheckPlayerEarnedGold(self):
		# money = 0
		# if self.LAST_GOLD_CHECK < fgGHGjjFHJghjfFG1545gGG.GetElk():
			# money = fgGHGjjFHJghjfFG1545gGG.GetElk() - self.LAST_GOLD_CHECK 
			# self.GOLD_EARNED = money
		
		
	def FormatTime(self, time):
		m, s = divmod(time, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)		
	
#-------------------Giftbox Begin------------------------------

class GiftBox(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")
			self.SetWindowName("GiftBox")
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)

	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.tooltipGift = self.TextToolTip()
		self.tooltipGift.Show()
		
	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "giftbox.py")
		except:
			import exception
			exception.Abort("GiftBox.LoadWindow.LoadObject")		

		self.giftBoxIcon = self.GetChild("GiftBox_Icon")
		self.giftBoxToolTip = self.GetChild("GiftBox_ToolTip")
	
	def Destroy(self):		
		self.giftBoxIcon = 0
		self.giftBoxToolTip = 0		
			
#-------------------Giftbox End------------------------------





class EnergyBar(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")
			self.SetWindowName("EnergyBar")
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)

	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.tooltipEnergy = self.TextToolTip()
		self.tooltipEnergy.Show()
		self.Hide()
		
	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "EnergyBar.py")
		except:
			import exception
			exception.Abort("EnergyBar.LoadWindow.LoadObject")

		self.energyEmpty = self.GetChild("EnergyGauge_Empty")
		self.energyHungry = self.GetChild("EnergyGauge_Hungry")
		self.energyFull = self.GetChild("EnergyGauge_Full")

		self.energyGaugeBoard = self.GetChild("EnergyGauge_Board")
		self.energyGaugeToolTip = self.GetChild("EnergyGauge_ToolTip")
		
		self.energyEmpty.Hide()
		self.energyHungry.Hide()
		self.energyFull.Hide()

		self.energyGaugeBoard.Hide()
		self.energyGaugeToolTip.Hide()

		self.Hide()
		
	def Destroy(self):		
		self.energyEmpty = None
		self.energyHungry = None
		self.energyFull = None
		self.energyGaugeBoard = 0
		self.energyGaugeToolTip = 0
		self.tooltipEnergy = 0

	## Gauge
	def RefreshStatus(self):
		pointEnergy = fgGHGjjFHJghjfFG1545gGG.GetStatus (fgGHGjjFHJghjfFG1545gGG.ENERGY)
		leftTimeEnergy = fgGHGjjFHJghjfFG1545gGG.GetStatus (fgGHGjjFHJghjfFG1545gGG.ENERGY_END_TIME) - app.GetGlobalTimeStamp()
		# 충기환 지속 시간 = 2시간.
		self.SetEnergy (pointEnergy, leftTimeEnergy, 7200)
			
	def SetEnergy (self, point, leftTime, maxTime):
		leftTime = max (leftTime, 0)
		maxTime = max (maxTime, 0)
			
		self.energyEmpty.Hide()
		self.energyHungry.Hide()
		self.energyFull.Hide()
	
		if leftTime == 0:
			self.energyEmpty.Show()
		elif ((leftTime * 100) / maxTime) < 15:
			self.energyHungry.Show()
		else:
			self.energyFull.Show()

		self.tooltipEnergy.SetText("                                  " + localeInfo.SecondToHM(leftTime) + " - Energie +" + str(point) + "%")

	def OnUpdate(self):
		if TRUE == self.energyGaugeToolTip.IsIn():
			self.RefreshStatus()
			self.tooltipEnergy.Show()
		else:
			self.tooltipEnergy.Hide()

class ExpandedTaskBar(ui.ScriptWindow):
	BUTTON_DRAGON_SOUL = 0
	def __init__(self):
		ui.Window.__init__(self)
		self.SetWindowName("ExpandedTaskBar")
	
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "ExpandedTaskBar.py")
		except:
			import exception
			exception.Abort("ExpandedTaskBar.LoadWindow.LoadObject")

		self.expandedTaskBarBoard = self.GetChild("ExpanedTaskBar_Board")

		self.toggleButtonDict = {}
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL] = self.GetChild("DragonSoulButton")
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL].SetParent(self)
	
	def SetTop(self):
		super(ExpandedTaskBar, self).SetTop()	
		for button in self.toggleButtonDict.values():
			button.SetTop()
 	
	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Close(self):
		self.Hide()
	
	def SetToolTipText(self, eButton, text):
		self.toggleButtonDict[eButton].SetToolTipText(text)
		
	def SetToggleButtonEvent(self, eButton, kEventFunc):
		self.toggleButtonDict[eButton].SetEvent(kEventFunc)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
	
class TaskBar(ui.ScriptWindow):

	BUTTON_CHARACTER = 0
	BUTTON_INVENTORY = 1
	BUTTON_MESSENGER = 2
	BUTTON_SYSTEM = 3
	BUTTON_CHAT = 4
	BUTTON_EXPAND = 4
	BUTTON_WARP = 5
	BUTTON_BONUS = 6
	BUTTON_EVENT = 7
	BUTTON_FORGE = 8
	BUTTON_HOF = 9
	BUTTON_QUEST = 10
	IS_EXPANDED = FALSE

	MOUSE_BUTTON_LEFT = 0
	MOUSE_BUTTON_RIGHT = 1
	NONE = 255

	EVENT_MOVE = 0
	EVENT_ATTACK = 1
	EVENT_MOVE_AND_ATTACK = 2
	EVENT_CAMERA = 3
	EVENT_SKILL = 4
	EVENT_AUTO = 5

	GAUGE_WIDTH = 95
	GAUGE_HEIGHT = 13

	QUICKPAGE_NUMBER_FILENAME = [
		"d:/ymir work/ui/game/taskbar/1.sub",
		"d:/ymir work/ui/game/taskbar/2.sub",
		"d:/ymir work/ui/game/taskbar/3.sub",
		"d:/ymir work/ui/game/taskbar/4.sub",
	]

	#gift icon show and hide
	def ShowGift(self):
		self.wndGiftBox.Show()
	
	def HideGift(self):
		self.wndGiftBox.Hide()

	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)

	class SkillButton(ui.SlotWindow):

		def __init__(self):
			ui.SlotWindow.__init__(self)

			self.event = 0
			self.arg = 0

			self.slotIndex = 0
			self.skillIndex = 0

			slotIndex = 0
			wndMgr.SetSlotBaseImage(self.hWnd, "d:/ymir work/ui/public/slot_base.sub", 1.0, 1.0, 1.0, 1.0)
			wndMgr.AppendSlot(self.hWnd, slotIndex, 0, 0, 32, 32)
			self.SetCoverButton(slotIndex,	"d:/ymir work/ui/public/slot_cover_button_01.sub",\
											"d:/ymir work/ui/public/slot_cover_button_02.sub",\
											"d:/ymir work/ui/public/slot_cover_button_03.sub",\
											"d:/ymir work/ui/public/slot_cover_button_04.sub", TRUE, FALSE)
			self.SetSize(32, 32)

		def __del__(self):
			ui.SlotWindow.__del__(self)

		def Destroy(self):
			if 0 != self.tooltipSkill:
				self.tooltipSkill.HideToolTip()

		def RefreshSkill(self):
			if 0 != self.slotIndex:
				self.SetSkill(self.slotIndex)

		def SetSkillToolTip(self, tooltip):
			self.tooltipSkill = tooltip

		def SetSkill(self, skillSlotNumber):
			slotNumber = 0
			skillIndex = fgGHGjjFHJghjfFG1545gGG.GetSkillIndex(skillSlotNumber)
			skillGrade = fgGHGjjFHJghjfFG1545gGG.GetSkillGrade(skillSlotNumber)
			skillLevel = fgGHGjjFHJghjfFG1545gGG.GetSkillLevel(skillSlotNumber)
			skillType = skill.GetSkillType(skillIndex)

			self.skillIndex = skillIndex
			if 0 == self.skillIndex:
				self.ClearSlot(slotNumber)
				return

			self.slotIndex = skillSlotNumber

			self.SetSkillSlotNew(slotNumber, skillIndex, skillGrade, skillLevel)
			self.SetSlotCountNew(slotNumber, skillGrade, skillLevel)

			## NOTE : CoolTime 체크
			if fgGHGjjFHJghjfFG1545gGG.IsSkillCoolTime(skillSlotNumber):
				(coolTime, elapsedTime) = fgGHGjjFHJghjfFG1545gGG.GetSkillCoolTime(skillSlotNumber)
				self.SetSlotCoolTime(slotNumber, coolTime, elapsedTime)

			## NOTE : Activate 되어 있다면 아이콘도 업데이트
			if fgGHGjjFHJghjfFG1545gGG.IsSkillActive(skillSlotNumber):
				self.ActivateSlot(slotNumber)

		def SetSkillEvent(self, event, arg=0):
			self.event = event
			self.arg = arg

		def GetSkillIndex(self):
			return self.skillIndex

		def GetSlotIndex(self):
			return self.slotIndex

		def Activate(self, coolTime):
			self.SetSlotCoolTime(0, coolTime)

			if skill.IsToggleSkill(self.skillIndex):
				self.ActivateSlot(0)

		def Deactivate(self):
			if skill.IsToggleSkill(self.skillIndex):
				self.DeactivateSlot(0)

		def OnOverInItem(self, dummy):
			self.tooltipSkill.SetSkill(self.skillIndex)

		def OnOverOutItem(self):
			self.tooltipSkill.HideToolTip()

		def OnSelectItemSlot(self, dummy):
			if 0 != self.event:
				if 0 != self.arg:
					self.event(self.arg)
				else:
					self.event()

	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"

		ui.ScriptWindow.__init__(self, "TOP_MOST")

		self.quickPageNumImageBox = None
		self.tooltipItem = 0
		self.tooltipSkill = 0
		self.mouseModeButtonList = [ ui.ScriptWindow("TOP_MOST"), ui.ScriptWindow("TOP_MOST") ]

		self.tooltipHP = self.TextToolTip()
		self.tooltipHP.Show()
		self.tooltipSP = self.TextToolTip()
		self.tooltipSP.Show()
		self.tooltipST = self.TextToolTip()
		self.tooltipST.Show()
		self.tooltipEXP = self.TextToolTip()
		self.tooltipEXP.Show()
		
		# self.buttonToolTip = self.ButtonToolTipWindow()
		
		self.skillCategoryNameList = [ "ACTIVE_1", "ACTIVE_2", "ACTIVE_3" ]
		self.skillPageStartSlotIndexDict = {
			"ACTIVE_1" : 1, 
			"ACTIVE_2" : 21, 
			"ACTIVE_3" : 41, 
		}

		self.selectSkillButtonList = []
		
		self.lastUpdateQuickSlot = 0
		self.SetWindowName("TaskBar")

	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()

			if constInfo.IN_GAME_SHOP_ENABLE:
				pyScrLoader.LoadScriptFile(self, "exscript/TaskBar.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/TaskBar.py")
			pyScrLoader.LoadScriptFile(self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT], "UIScript/MouseButtonWindow.py")
			pyScrLoader.LoadScriptFile(self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT], "UIScript/RightMouseButtonWindow.py")
		except:
			import exception
			exception.Abort("TaskBar.LoadWindow.LoadObject")

		self.quickslot = []
		self.quickslot.append(self.GetChild("quick_slot_1"))
		self.quickslot.append(self.GetChild("quick_slot_2"))
		for slot in self.quickslot:
			slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptyQuickSlot))
			slot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemQuickSlot))
			slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemQuickSlot))
			slot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		toggleButtonDict = {}
		toggleButtonDict[TaskBar.BUTTON_CHARACTER]=self.GetChild("CharacterButton")
		toggleButtonDict[TaskBar.BUTTON_INVENTORY]=self.GetChild("InventoryButton")
		toggleButtonDict[TaskBar.BUTTON_MESSENGER]=self.GetChild("MessengerButton")
		toggleButtonDict[TaskBar.BUTTON_SYSTEM]=self.GetChild("SystemButton")
		toggleButtonDict[TaskBar.BUTTON_WARP]=self.GetChild("WarpButton")
		toggleButtonDict[TaskBar.BUTTON_BONUS]=self.GetChild("BonusBoardButton")
		toggleButtonDict[TaskBar.BUTTON_EVENT]=self.GetChild("CalenderButton")
		toggleButtonDict[TaskBar.BUTTON_FORGE]=self.GetChild("ForgeGuideButton")
		toggleButtonDict[TaskBar.BUTTON_HOF]=self.GetChild("HallOfFameButton")
		
		
		
		
		# BUTTON_BONUS
		toggleButtonDict[TaskBar.BUTTON_QUEST]=self.GetChild("QuestButton")
		
		# ChatButton, ExpandButton 둘 중 하나는 반드시 존재한다.
		try:
			toggleButtonDict[TaskBar.BUTTON_CHAT]=self.GetChild("ChatButton")
		except:
			toggleButtonDict[TaskBar.BUTTON_EXPAND]=self.GetChild("ExpandButton")
			TaskBar.IS_EXPANDED = TRUE
		

		if localeInfo.IsARABIC():
			systemButton = toggleButtonDict[TaskBar.BUTTON_SYSTEM]
			if systemButton.ToolTipText:
				tx, ty = systemButton.ToolTipText.GetLocalPosition()
				tw = systemButton.ToolTipText.GetWidth() 
				systemButton.ToolTipText.SetPosition(-tw/2, ty)


		expGauge = []
		expGauge.append(self.GetChild("EXPGauge_01"))
		expGauge.append(self.GetChild("EXPGauge_02"))
		expGauge.append(self.GetChild("EXPGauge_03"))
		expGauge.append(self.GetChild("EXPGauge_04"))

		for exp in expGauge:
			exp.SetSize(0, 0)

		self.quickPageNumImageBox=self.GetChild("QuickPageNumber")

		self.GetChild("QuickPageUpButton").SetEvent(ui.__mem_func__(self.__OnClickQuickPageUpButton))
		self.GetChild("QuickPageDownButton").SetEvent(ui.__mem_func__(self.__OnClickQuickPageDownButton))
		
		
		self.GetChild("Gauge_Board").Hide()
		########Anti Exp Button by Sanii##########
		
		#self.antiexp		= self.GetChild("AntiButton")
		#self.antiexp.SetEvent(ui.__mem_func__(self.AntiExp))
		
		#if constInfo.ANTI_EXP_STATE == 1:
			#self.antiexp.SetText("-")
			#self.antiexp.SetToolTipText("Anti-Erfahrung deaktivieren")
		#else:
			#self.antiexp.SetText("+")
			#self.antiexp.SetToolTipText("Anti-Erfahrung aktivieren")
		
		mouseLeftButtonModeButton = self.GetChild("LeftMouseButton")
		mouseRightButtonModeButton = self.GetChild("RightMouseButton")
		mouseLeftButtonModeButton.SetEvent(ui.__mem_func__(self.ToggleLeftMouseButtonModeWindow))		
		mouseRightButtonModeButton.SetEvent(ui.__mem_func__(self.ToggleRightMouseButtonModeWindow))
		self.curMouseModeButton = [ mouseLeftButtonModeButton, mouseRightButtonModeButton ]

		(xLocalRight, yLocalRight) = mouseRightButtonModeButton.GetLocalPosition()
		self.curSkillButton = self.SkillButton()
		self.curSkillButton.SetParent(self)
		self.curSkillButton.SetPosition(xLocalRight, 3)
		self.curSkillButton.SetSkillEvent(ui.__mem_func__(self.ToggleRightMouseButtonModeWindow))
		self.curSkillButton.Hide()

		(xLeft, yLeft) = mouseLeftButtonModeButton.GetGlobalPosition()
		(xRight, yRight) = mouseRightButtonModeButton.GetGlobalPosition()
		leftModeButtonList = self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT]
		leftModeButtonList.SetPosition(xLeft, yLeft - leftModeButtonList.GetHeight()-5)
		rightModeButtonList = self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT]
		rightModeButtonList.SetPosition(xRight - rightModeButtonList.GetWidth() + 32, yRight - rightModeButtonList.GetHeight()-5)
		rightModeButtonList.GetChild("button_skill").SetEvent(lambda adir=self.MOUSE_BUTTON_RIGHT, aevent=self.EVENT_SKILL: self.SelectMouseButtonEvent(adir, aevent))
		rightModeButtonList.GetChild("button_skill").Hide()

		mouseImage = ui.ImageBox("TOP_MOST")
		mouseImage.AddFlag("float")
		mouseImage.LoadImage("d:/ymir work/ui/game/taskbar/mouse_button_camera_01.sub")
		mouseImage.SetPosition(xRight, wndMgr.GetScreenHeight() - 34)
		mouseImage.Hide()
		self.mouseImage = mouseImage

		dir = self.MOUSE_BUTTON_LEFT
		wnd = self.mouseModeButtonList[dir]
		wnd.GetChild("button_move_and_attack").SetEvent(lambda adir=dir, aevent=self.EVENT_MOVE_AND_ATTACK: self.SelectMouseButtonEvent(adir, aevent))
		wnd.GetChild("button_auto_attack").SetEvent(lambda adir=dir, aevent=self.EVENT_AUTO: self.SelectMouseButtonEvent(adir, aevent))
		wnd.GetChild("button_camera").SetEvent(lambda adir=dir, aevent=self.EVENT_CAMERA: self.SelectMouseButtonEvent(adir, aevent))

		dir = self.MOUSE_BUTTON_RIGHT
		wnd = self.mouseModeButtonList[dir]
		wnd.GetChild("button_move_and_attack").SetEvent(lambda adir=dir, aevent=self.EVENT_MOVE_AND_ATTACK: self.SelectMouseButtonEvent(adir, aevent))
		wnd.GetChild("button_camera").SetEvent(lambda adir=dir, aevent=self.EVENT_CAMERA: self.SelectMouseButtonEvent(adir, aevent))

		self.toggleButtonDict = toggleButtonDict
		self.expGauge = expGauge

		if constInfo.IN_GAME_SHOP_ENABLE:
			self.rampageGauge1  = self.GetChild("RampageGauge")
			self.rampageGauge1.OnMouseOverIn = ui.__mem_func__(self.__RampageGauge_OverIn)
			self.rampageGauge2 = self.GetChild("RampageGauge2")
			self.rampageGauge2.OnMouseOverOut = ui.__mem_func__(self.__RampageGauge_OverOut)
			self.rampageGauge2.OnMouseLeftButtonUp = ui.__mem_func__(self.__RampageGauge_Click)
			self.__RampageGauge_OverOut()

		self.hpGauge = self.GetChild("HPGauge")
		self.mpGauge = self.GetChild("SPGauge")
		self.stGauge = self.GetChild("STGauge")
		self.hpRecoveryGaugeBar = self.GetChild("HPRecoveryGaugeBar")
		self.spRecoveryGaugeBar = self.GetChild("SPRecoveryGaugeBar")

		self.hpGaugeBoard=self.GetChild("HPGauge_Board")
		self.mpGaugeBoard=self.GetChild("SPGauge_Board")
		self.stGaugeBoard=self.GetChild("STGauge_Board")
		self.expGaugeBoard=self.GetChild("EXP_Gauge_Board")
		
		#giftbox object
		wndGiftBox = GiftBox()
		wndGiftBox.LoadWindow()
		self.wndGiftBox = wndGiftBox

		wndPlayerFrame = PlayerFrame()
		wndPlayerFrame.LoadWindow()
		self.wndPlayerFrame = wndPlayerFrame
		self.wndPlayerFrame.SetPosition(systemSetting.GetPlayerFrameX(), systemSetting.GetPlayerFrameY())
		
		self.PointArrowWarp = exterminatus.PointArrow()
		# self.PointArrowWarp.SetParent(self)
		self.PointArrowWarp.SetPosition(115,wndMgr.GetScreenHeight() - 80)
		self.PointArrowWarp.Hide()
		
		
		self.wndButtonToolTip = ButtonToolTipWindow()
		# self.buttonToolTip = self.ButtonToolTipWindow()
		self.toggleButtonDict[TaskBar.BUTTON_CHARACTER].ShowToolTip = lambda arg=TaskBar.BUTTON_CHARACTER: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_CHARACTER].HideToolTip = lambda arg=TaskBar.BUTTON_CHARACTER: self.__OverOutTaskbarButton()
		
		self.toggleButtonDict[TaskBar.BUTTON_INVENTORY].ShowToolTip = lambda arg=TaskBar.BUTTON_INVENTORY: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_INVENTORY].HideToolTip = lambda arg=TaskBar.BUTTON_INVENTORY: self.__OverOutTaskbarButton()
		
		self.toggleButtonDict[TaskBar.BUTTON_MESSENGER].ShowToolTip = lambda arg=TaskBar.BUTTON_MESSENGER: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_MESSENGER].HideToolTip = lambda arg=TaskBar.BUTTON_MESSENGER: self.__OverOutTaskbarButton()
		
		self.toggleButtonDict[TaskBar.BUTTON_SYSTEM].ShowToolTip = lambda arg=TaskBar.BUTTON_SYSTEM: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_SYSTEM].HideToolTip = lambda arg=TaskBar.BUTTON_SYSTEM: self.__OverOutTaskbarButton()
		
		self.toggleButtonDict[TaskBar.BUTTON_WARP].ShowToolTip = lambda arg=TaskBar.BUTTON_WARP: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_WARP].HideToolTip = lambda arg=TaskBar.BUTTON_WARP: self.__OverOutTaskbarButton()
		
		self.toggleButtonDict[TaskBar.BUTTON_BONUS].ShowToolTip = lambda arg=TaskBar.BUTTON_BONUS: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_BONUS].HideToolTip = lambda arg=TaskBar.BUTTON_BONUS: self.__OverOutTaskbarButton()

		self.toggleButtonDict[TaskBar.BUTTON_EVENT].ShowToolTip = lambda arg=TaskBar.BUTTON_EVENT: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_EVENT].HideToolTip = lambda arg=TaskBar.BUTTON_EVENT: self.__OverOutTaskbarButton()

		self.toggleButtonDict[TaskBar.BUTTON_FORGE].ShowToolTip = lambda arg=TaskBar.BUTTON_FORGE: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_FORGE].HideToolTip = lambda arg=TaskBar.BUTTON_FORGE: self.__OverOutTaskbarButton()

		self.toggleButtonDict[TaskBar.BUTTON_HOF].ShowToolTip = lambda arg=TaskBar.BUTTON_HOF: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_HOF].HideToolTip = lambda arg=TaskBar.BUTTON_HOF: self.__OverOutTaskbarButton()

		self.toggleButtonDict[TaskBar.BUTTON_QUEST].ShowToolTip = lambda arg=TaskBar.BUTTON_QUEST: self.__OverInTaskbarButton(arg)
		self.toggleButtonDict[TaskBar.BUTTON_QUEST].HideToolTip = lambda arg=TaskBar.BUTTON_QUEST: self.__OverOutTaskbarButton()

		
		self.__LoadMouseSettings()
		self.RefreshStatus()
		self.RefreshQuickSlot()
		self.InitYamatoUI()
		self.CheckIfPlayerIsTutorial()

	def __OverInTaskbarButton(self,button):
		self.wndButtonToolTip.Open(button)
		
		if button == TaskBar.BUTTON_INVENTORY:
			money = fgGHGjjFHJghjfFG1545gGG.GetElk()
			
			self.wndButtonToolTip.AppendSpaceLine()
			self.wndButtonToolTip.AppendCurrencyInfo("Yang:",constInfo.NumberToPointString(money))
			self.wndButtonToolTip.AppendCurrencyInfo("Achievement-Points:",constInfo.NumberToPointString(constInfo.aps))
			self.wndButtonToolTip.AppendCurrencyInfo("Dungeonpoints:",constInfo.NumberToPointString(0))
			self.wndButtonToolTip.AppendSpaceLine()
		
	def __OverOutTaskbarButton(self):
		self.wndButtonToolTip.Close()

	
	def CheckIfPlayerIsTutorial(self):
		if background.GetCurrentMapName() == "map_dungeon_tutorial_hall":
			self.toggleButtonDict[TaskBar.BUTTON_WARP].Disable()
		else:
			self.toggleButtonDict[TaskBar.BUTTON_WARP].Enable()
	
	def InitYamatoUI(self):
		self.hpGauge.Hide()
		self.mpGauge.Hide()
		self.stGauge.Hide()
		self.hpRecoveryGaugeBar.Hide()
		self.spRecoveryGaugeBar.Hide()

		self.hpGaugeBoard.Hide()
		self.mpGaugeBoard.Hide()
		self.stGaugeBoard.Hide()
		self.expGaugeBoard.Hide()		
		self.rampageGauge2.Hide()
		self.rampageGauge1.Hide()
		for exp in self.expGauge:
			exp.Hide()
			
		self.wndPlayerFrame.Show()
		
		# self.toggleButtonDict[TaskBar.BUTTON_WARP].Disable()
		
	# def EnableWarpButton(self):
		# self.toggleButtonDict[TaskBar.BUTTON_WARP].Enable()
		
	def __RampageGauge_OverIn(self):
		print "rampage_over_in"
		self.rampageGauge2.Show()
		self.rampageGauge1.Hide()

	def __RampageGauge_OverOut(self):
		print "rampage_over_out"
		self.rampageGauge2.Hide()
		self.rampageGauge1.Show()

	def __RampageGauge_Click(self):
		print "rampage_up"
		if self.mallShowEvent:
			self.mallShowEvent()
		else:
			GFHhg54GHGhh45GHGH.SendChatPacket("/in_game_mall")
			
	def SetMallShowEvent(self, event):
		self.mallShowEvent = event

	def __LoadMouseSettings(self):
		try:
			LoadMouseButtonSettings()
			(mouseLeftButtonEvent, mouseRightButtonEvent) = GetMouseButtonSettings()
			if not self.__IsInSafeMouseButtonSettingRange(mouseLeftButtonEvent) or not self.__IsInSafeMouseButtonSettingRange(mouseRightButtonEvent):
					raise RuntimeError, "INVALID_MOUSE_BUTTON_SETTINGS"
		except:
			InitMouseButtonSettings(self.EVENT_MOVE_AND_ATTACK, self.EVENT_CAMERA)
			(mouseLeftButtonEvent, mouseRightButtonEvent) = GetMouseButtonSettings()

		try:
			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_LEFT,	mouseLeftButtonEvent)
			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_RIGHT,	mouseRightButtonEvent)
		except:
			InitMouseButtonSettings(self.EVENT_MOVE_AND_ATTACK, self.EVENT_CAMERA)
			(mouseLeftButtonEvent, mouseRightButtonEvent) = GetMouseButtonSettings()

			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_LEFT,	mouseLeftButtonEvent)
			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_RIGHT,	mouseRightButtonEvent)



	def __IsInSafeMouseButtonSettingRange(self, arg):
		return arg >= self.EVENT_MOVE and arg <= self.EVENT_AUTO

	def Destroy(self):		
		SaveMouseButtonSettings()

		self.ClearDictionary()
		self.mouseModeButtonList[0].ClearDictionary()
		self.mouseModeButtonList[1].ClearDictionary()
		self.mouseModeButtonList = 0
		self.curMouseModeButton = 0
		self.curSkillButton = 0
		self.selectSkillButtonList = 0


		self.expGauge = None
		self.hpGauge = None
		self.mpGauge = None
		self.stGauge = None
		self.hpRecoveryGaugeBar = None
		self.spRecoveryGaugeBar = None
	
		self.tooltipItem = 0
		self.tooltipSkill = 0
		self.mallShowEvent = None
		self.quickslot = 0
		self.toggleButtonDict = 0

		self.hpGaugeBoard = 0
		self.mpGaugeBoard = 0
		self.stGaugeBoard = 0
		
		self.expGaugeBoard = 0

		self.tooltipHP = 0
		self.tooltipSP = 0
		self.tooltipST = 0
		self.tooltipEXP = 0

		self.mouseImage = None

	def __OnClickQuickPageUpButton(self):
		fgGHGjjFHJghjfFG1545gGG.SetQuickPage(fgGHGjjFHJghjfFG1545gGG.GetQuickPage()-1)

	def __OnClickQuickPageDownButton(self):
		fgGHGjjFHJghjfFG1545gGG.SetQuickPage(fgGHGjjFHJghjfFG1545gGG.GetQuickPage()+1)

	def SetToggleButtonEvent(self, eButton, kEventFunc):
		self.toggleButtonDict[eButton].SetEvent(kEventFunc)

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SetSkillToolTip(self, tooltipSkill):
		self.tooltipSkill = tooltipSkill
		self.curSkillButton.SetSkillToolTip(self.tooltipSkill)

	## Mouse Image
	def ShowMouseImage(self):
		self.mouseImage.SetTop()
		self.mouseImage.Show()

	def HideMouseImage(self):
		fgGHGjjFHJghjfFG1545gGG.SetQuickCameraMode(FALSE)
		self.mouseImage.Hide()
	
	def ShowPointArrowWarp(self):
		self.PointArrowWarp.Show()
		
	def QuestWindowBlink(self):
		self.toggleButtonDict[TaskBar.BUTTON_QUEST].Flash()
	
	## Gauge
	def RefreshStatus(self):
		curHP = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.HP)
		maxHP = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.MAX_HP)
		curSP = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.SP)
		maxSP = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.MAX_SP)
		curEXP = unsigned32(fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.EXP))
		nextEXP = unsigned32(fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.NEXT_EXP))
		recoveryHP = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.HP_RECOVERY)
		recoverySP = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.SP_RECOVERY)
		
		self.RefreshStamina()

		self.wndPlayerFrame.SetHP(curHP, recoveryHP, maxHP)
		self.wndPlayerFrame.SetMP(curSP, recoverySP, maxSP)
		self.wndPlayerFrame.SetEXP(curEXP, nextEXP)
		
	def RefreshStamina(self):
		curST = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.STAMINA)
		maxST = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.MAX_STAMINA)
		self.SetST(curST, maxST)

	def RefreshSkill(self):
		self.curSkillButton.RefreshSkill()
		for button in self.selectSkillButtonList:
			button.RefreshSkill()

	def SetHP(self, curPoint, recoveryPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.hpGauge.SetPercentage(curPoint, maxPoint)
			self.tooltipHP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_HP, curPoint, maxPoint))

			if 0 == recoveryPoint:
				self.hpRecoveryGaugeBar.Hide()
			else:
				destPoint = min(maxPoint, curPoint + recoveryPoint)
				newWidth = int(self.GAUGE_WIDTH * (float(destPoint) / float(maxPoint)))
				self.hpRecoveryGaugeBar.SetSize(newWidth, self.GAUGE_HEIGHT)
				self.hpRecoveryGaugeBar.Show()

	def SetSP(self, curPoint, recoveryPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.mpGauge.SetPercentage(curPoint, maxPoint)
			self.tooltipSP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_SP, curPoint, maxPoint))

			if 0 == recoveryPoint:
				self.spRecoveryGaugeBar.Hide()
			else:
				destPoint = min(maxPoint, curPoint + recoveryPoint)
				newWidth = int(self.GAUGE_WIDTH * (float(destPoint) / float(maxPoint)))
				self.spRecoveryGaugeBar.SetSize(newWidth, self.GAUGE_HEIGHT)
				self.spRecoveryGaugeBar.Show()

	def SetST(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.stGauge.SetPercentage(curPoint, maxPoint)
			self.tooltipST.SetText("%s : %d / %d" % (localeInfo.TASKBAR_ST, curPoint, maxPoint))

	def SetExperience(self, curPoint, maxPoint):

		curPoint = min(curPoint, maxPoint)
		curPoint = max(curPoint, 0)
		maxPoint = max(maxPoint, 0)

		quarterPoint = maxPoint / 4
		FullCount = 0

		if 0 != quarterPoint:
			FullCount = min(4, curPoint / quarterPoint)

		for i in xrange(4):
			self.expGauge[i].Hide()

		for i in xrange(FullCount):
			self.expGauge[i].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.expGauge[i].Show()

		if 0 != quarterPoint:
			if FullCount < 4:
				Percentage = float(curPoint % quarterPoint) / quarterPoint - 1.0
				self.expGauge[FullCount].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.expGauge[FullCount].Show()

		#####
		self.tooltipEXP.SetText("%s : %.2f%%" % (localeInfo.TASKBAR_EXP, float(curPoint) / max(1, float(maxPoint)) * 100))
	
		
	## QuickSlot
	def RefreshQuickSlot(self):

		pageNum = fgGHGjjFHJghjfFG1545gGG.GetQuickPage()

		try:
			self.quickPageNumImageBox.LoadImage(TaskBar.QUICKPAGE_NUMBER_FILENAME[pageNum])
		except:
			pass

		startNumber = 0
		for slot in self.quickslot:

			for i in xrange(4):

				slotNumber = i+startNumber

				(Type, Position) = fgGHGjjFHJghjfFG1545gGG.GetLocalQuickSlot(slotNumber)

				if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_NONE == Type:
					slot.ClearSlot(slotNumber)
					continue

				if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == Type:

					itemIndex = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(Position)
					itemCount = fgGHGjjFHJghjfFG1545gGG.GetItemCount(Position)
					if itemCount <= 1:
						itemCount = 0
					
					## 자동물약 (#72723, #72724) 특수처리 - 아이템인데도 슬롯에 활성화/비활성화 표시를 위한 작업임 - [hyo]
					if constInfo.IS_AUTO_POTION(itemIndex):
						# metinSocket - [0] : 활성화 여부, [1] : 사용한 양, [2] : 최대 용량
						metinSocket = [fgGHGjjFHJghjfFG1545gGG.GetItemMetinSocket(Position, j) for j in xrange(fgGHGjjFHJghjfFG1545gGG.METIN_SOCKET_MAX_NUM)]
						
						if 0 != int(metinSocket[0]):
							slot.ActivateSlot(slotNumber)
						else:
							slot.DeactivateSlot(slotNumber)
					
					slot.SetItemSlot(slotNumber, itemIndex, itemCount)

				elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SKILL == Type:

					skillIndex = fgGHGjjFHJghjfFG1545gGG.GetSkillIndex(Position)
					if 0 == skillIndex:
						slot.ClearSlot(slotNumber)
						continue

					skillType = skill.GetSkillType(skillIndex)
					if skill.SKILL_TYPE_GUILD == skillType:
						import guild
						skillGrade = 0
						skillLevel = guild.GetSkillLevel(Position)

					else:
						skillGrade = fgGHGjjFHJghjfFG1545gGG.GetSkillGrade(Position)
						skillLevel = fgGHGjjFHJghjfFG1545gGG.GetSkillLevel(Position)

					slot.SetSkillSlotNew(slotNumber, skillIndex, skillGrade, skillLevel)
					slot.SetSlotCountNew(slotNumber, skillGrade, skillLevel)
					slot.SetCoverButton(slotNumber)

					## NOTE : CoolTime 체크
					if fgGHGjjFHJghjfFG1545gGG.IsSkillCoolTime(Position):
						(coolTime, elapsedTime) = fgGHGjjFHJghjfFG1545gGG.GetSkillCoolTime(Position)
						slot.SetSlotCoolTime(slotNumber, coolTime, elapsedTime)

					## NOTE : Activate 되어 있다면 아이콘도 업데이트
					if fgGHGjjFHJghjfFG1545gGG.IsSkillActive(Position):
						slot.ActivateSlot(slotNumber)

				elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_EMOTION == Type:

					emotionIndex = Position
					slot.SetEmotionSlot(slotNumber, emotionIndex)
					slot.SetCoverButton(slotNumber)
					slot.SetSlotCount(slotNumber, 0)

			slot.RefreshSlot()
			startNumber += 4

	def canAddQuickSlot(self, Type, slotNumber):

		if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == Type:

			itemIndex = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(slotNumber)
			return item.CanAddToQuickSlotItem(itemIndex)

		return TRUE

	def AddQuickSlot(self, localSlotIndex):
		AttachedSlotType = mouseModule.mouseController.GetAttachedType()
		AttachedSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
		AttachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

		if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_QUICK_SLOT == AttachedSlotType:
			fgGHGjjFHJghjfFG1545gGG.RequestMoveGlobalQuickSlotToLocalQuickSlot(AttachedSlotNumber, localSlotIndex)

		elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_EMOTION == AttachedSlotType:

			fgGHGjjFHJghjfFG1545gGG.RequestAddLocalQuickSlot(localSlotIndex, AttachedSlotType, AttachedItemIndex)

		elif TRUE == self.canAddQuickSlot(AttachedSlotType, AttachedSlotNumber):

			## Online Code
			fgGHGjjFHJghjfFG1545gGG.RequestAddLocalQuickSlot(localSlotIndex, AttachedSlotType, AttachedSlotNumber)
		
		mouseModule.mouseController.DeattachObject()
		self.RefreshQuickSlot()

	def SelectEmptyQuickSlot(self, slotIndex):

		if TRUE == mouseModule.mouseController.isAttached():
			self.AddQuickSlot(slotIndex)

	def SelectItemQuickSlot(self, localQuickSlotIndex):

		if TRUE == mouseModule.mouseController.isAttached():
			self.AddQuickSlot(localQuickSlotIndex)

		else:
			globalQuickSlotIndex=fgGHGjjFHJghjfFG1545gGG.LocalQuickSlotIndexToGlobalQuickSlotIndex(localQuickSlotIndex)
			mouseModule.mouseController.AttachObject(self, fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_QUICK_SLOT, globalQuickSlotIndex, globalQuickSlotIndex)

	def UnselectItemQuickSlot(self, localSlotIndex):

		if FALSE == mouseModule.mouseController.isAttached():
			fgGHGjjFHJghjfFG1545gGG.RequestUseLocalQuickSlot(localSlotIndex)
			return

		elif mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()
			return


	def OnUseSkill(self, usedSlotIndex, coolTime):

		QUICK_SLOT_SLOT_COUNT = 4
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Activate(coolTime)

		## Quick Slot
		for slotWindow in self.quickslot:

			for i in xrange(QUICK_SLOT_SLOT_COUNT):

				(Type, Position) = fgGHGjjFHJghjfFG1545gGG.GetLocalQuickSlot(slotIndex)

				if Type == fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SKILL:
					if usedSlotIndex == Position:
						slotWindow.SetSlotCoolTime(slotIndex, coolTime)
						return

				slotIndex += 1

	def OnActivateSkill(self, usedSlotIndex):
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Deactivate()

		## Quick Slot
		for slotWindow in self.quickslot:

			for i in xrange(4):

				(Type, Position) = fgGHGjjFHJghjfFG1545gGG.GetLocalQuickSlot(slotIndex)

				if Type == fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SKILL:
					if usedSlotIndex == Position:
						slotWindow.ActivateSlot(slotIndex)
						return

				slotIndex += 1

	def OnDeactivateSkill(self, usedSlotIndex):
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Deactivate()

		## Quick Slot
		for slotWindow in self.quickslot:

			for i in xrange(4):

				(Type, Position) = fgGHGjjFHJghjfFG1545gGG.GetLocalQuickSlot(slotIndex)

				if Type == fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SKILL:
					if usedSlotIndex == Position:
						slotWindow.DeactivateSlot(slotIndex)
						return

				slotIndex += 1

	## ToolTip
	def OverInItem(self, slotNumber):
		if mouseModule.mouseController.isAttached():
			return

		(Type, Position) = fgGHGjjFHJghjfFG1545gGG.GetLocalQuickSlot(slotNumber)

		if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == Type:
			self.tooltipItem.SetInventoryItem(Position)
			self.tooltipSkill.HideToolTip()

		elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_SKILL == Type:

			skillIndex = fgGHGjjFHJghjfFG1545gGG.GetSkillIndex(Position)
			skillType = skill.GetSkillType(skillIndex)

			if skill.SKILL_TYPE_GUILD == skillType:
				import guild
				skillGrade = 0
				skillLevel = guild.GetSkillLevel(Position)

			else:
				skillGrade = fgGHGjjFHJghjfFG1545gGG.GetSkillGrade(Position)
				skillLevel = fgGHGjjFHJghjfFG1545gGG.GetSkillLevel(Position)

			self.tooltipSkill.SetSkillNew(Position, skillIndex, skillGrade, skillLevel)
			self.tooltipItem.HideToolTip()

	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()
		if 0 != self.tooltipSkill:
			self.tooltipSkill.HideToolTip()

	def OnUpdate(self):
		if app.GetGlobalTime() - self.lastUpdateQuickSlot > 500:
			self.lastUpdateQuickSlot = app.GetGlobalTime()
			self.RefreshQuickSlot()

		if TRUE == self.hpGaugeBoard.IsIn():
			self.tooltipHP.Show()
		else:
			self.tooltipHP.Hide()

		if TRUE == self.mpGaugeBoard.IsIn():
			self.tooltipSP.Show()
		else:
			self.tooltipSP.Hide()

		if TRUE == self.stGaugeBoard.IsIn():
			self.tooltipST.Show()
		else:
			self.tooltipST.Hide()
		
		if TRUE == self.expGaugeBoard.IsIn():
			self.tooltipEXP.Show()
		else:
			self.tooltipEXP.Hide()
		
	## Skill
	def ToggleLeftMouseButtonModeWindow(self):

		wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT]

		if TRUE == wndMouseButtonMode.IsShow():

			wndMouseButtonMode.Hide()

		else:
			wndMouseButtonMode.Show()

	def ToggleRightMouseButtonModeWindow(self):

		wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT]

		if TRUE == wndMouseButtonMode.IsShow():

			wndMouseButtonMode.Hide()
			self.CloseSelectSkill()

		else:
			wndMouseButtonMode.Show()
			self.OpenSelectSkill()

	def OpenSelectSkill(self):

		PAGE_SLOT_COUNT = 6

		(xSkillButton, y) = self.curSkillButton.GetGlobalPosition()
		y -= (37 + 32 + 1)

		for key in self.skillCategoryNameList:

			appendCount = 0
			startNumber = self.skillPageStartSlotIndexDict[key]
			x = xSkillButton

			getSkillIndex=fgGHGjjFHJghjfFG1545gGG.GetSkillIndex
			getSkillLevel=fgGHGjjFHJghjfFG1545gGG.GetSkillLevel
			for i in xrange(PAGE_SLOT_COUNT):

				skillIndex = getSkillIndex(startNumber+i)
				skillLevel = getSkillLevel(startNumber+i)

				if 0 == skillIndex:
					continue
				if 0 == skillLevel:
					continue
				if skill.IsStandingSkill(skillIndex):
					continue

				## FIXME : 스킬 하나당 슬롯 하나씩 할당하는건 아무리 봐도 부하가 크다.
				##         이 부분은 시간을 나면 고치도록. - [levites]
				skillButton = self.SkillButton()
				skillButton.SetSkill(startNumber+i)
				skillButton.SetPosition(x, y)
				skillButton.SetSkillEvent(ui.__mem_func__(self.CloseSelectSkill), startNumber+i+1)
				skillButton.SetSkillToolTip(self.tooltipSkill)
				skillButton.SetTop()
				skillButton.Show()
				self.selectSkillButtonList.append(skillButton)

				appendCount += 1
				x -= 32

			if appendCount > 0:
				y -= 32

	def CloseSelectSkill(self, slotIndex=-1):

		self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT].Hide()
		for button in self.selectSkillButtonList:
			button.Destroy()

		self.selectSkillButtonList = []

		if -1 != slotIndex:
			self.curSkillButton.Show()
			self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Hide()
			fgGHGjjFHJghjfFG1545gGG.SetMouseFunc(fgGHGjjFHJghjfFG1545gGG.MBT_RIGHT, fgGHGjjFHJghjfFG1545gGG.MBF_SKILL)
			fgGHGjjFHJghjfFG1545gGG.ChangeCurrentSkillNumberOnly(slotIndex-1)
		else:
			self.curSkillButton.Hide()
			self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Show()

	def SelectMouseButtonEvent(self, dir, event):
		SetMouseButtonSetting(dir, event)

		self.CloseSelectSkill()
		self.mouseModeButtonList[dir].Hide()

		btn = 0
		type = self.NONE
		func = self.NONE
		tooltip_text = ""		
		
		if self.MOUSE_BUTTON_LEFT == dir:
			type = fgGHGjjFHJghjfFG1545gGG.MBT_LEFT

		elif self.MOUSE_BUTTON_RIGHT == dir:
			type = fgGHGjjFHJghjfFG1545gGG.MBT_RIGHT

		if self.EVENT_MOVE == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_move")
			func = fgGHGjjFHJghjfFG1545gGG.MBF_MOVE
			tooltip_text = localeInfo.TASKBAR_MOVE
		elif self.EVENT_ATTACK == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_attack")
			func = fgGHGjjFHJghjfFG1545gGG.MBF_ATTACK
			tooltip_text = localeInfo.TASKBAR_ATTACK
		elif self.EVENT_AUTO == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_auto_attack")
			func = fgGHGjjFHJghjfFG1545gGG.MBF_AUTO
			tooltip_text = localeInfo.TASKBAR_AUTO
		elif self.EVENT_MOVE_AND_ATTACK == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_move_and_attack")
			func = fgGHGjjFHJghjfFG1545gGG.MBF_SMART
			tooltip_text = localeInfo.TASKBAR_ATTACK
		elif self.EVENT_CAMERA == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_camera")
			func = fgGHGjjFHJghjfFG1545gGG.MBF_CAMERA
			tooltip_text = localeInfo.TASKBAR_CAMERA
		elif self.EVENT_SKILL == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_skill")
			func = fgGHGjjFHJghjfFG1545gGG.MBF_SKILL
			tooltip_text = localeInfo.TASKBAR_SKILL

		if 0 != btn:
			self.curMouseModeButton[dir].SetToolTipText(tooltip_text, 0, -18)
			self.curMouseModeButton[dir].SetUpVisual(btn.GetUpVisualFileName())
			self.curMouseModeButton[dir].SetOverVisual(btn.GetOverVisualFileName())
			self.curMouseModeButton[dir].SetDownVisual(btn.GetDownVisualFileName())
			self.curMouseModeButton[dir].Show()

		fgGHGjjFHJghjfFG1545gGG.SetMouseFunc(type, func)

	def OnChangeCurrentSkill(self, skillSlotNumber):
		self.curSkillButton.SetSkill(skillSlotNumber)
		self.curSkillButton.Show()
		self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Hide()
		
		
	########Anti Exp Button by Sanii##########		
	def AntiExp(self):
		import constInfo
		import event
		import net
		qid = constInfo.ANTI_EXP
		state = constInfo.ANTI_EXP_STATE
		if state == 0:
			self.antiexp.SetText("-")
			self.antiexp.SetToolTipText("Anti-Erfahrung deaktivieren")
			event.QuestButtonClick(qid)
		else:
			self.antiexp.SetText("+")
			self.antiexp.SetToolTipText("Anti-Erfahrung aktivieren")
			event.QuestButtonClick(qid)
	##########################################

