import ui
import localeInfo
import chr
import item
import app
import skill
import fgGHGjjFHJghjfFG1545gGG
import uiToolTip
import math
import constInfo
import chat
import GFHhg54GHGhh45GHGH
import uiCommon
if app.ENABLE_NEW_AFFECT_POTION:				
	AFFECT_POTION = {
		"affect"  : {
			0 : 303,
			1 : 304,
			2 : 305,
			3 : 306,
			4 : 307,
			5 : 308,
		},
		#"modulePython"  : {
			#0 : str(pkAffect),
			#1 : int(pRemove_vegas),
		#},
		"image"  : {
			0 : "icon/item/50821.tga",
			1 : "icon/item/50822.tga",
			2 : "icon/item/50823.tga",
			3 : "icon/item/50824.tga",
			4 : "icon/item/50825.tga",
			5 : "icon/item/50826.tga",
		},
	}
	
	
biologist_bonus = []

"""


append = {
	"progress_index" : 1,
	"


}


"""

	
class BiologistAttributeImage(ui.ExpandedImageBox):

	FILE_PATH = "d:/ymir work/ui/bai.tga"
	FILE_DICT = {}

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)
		self.toolTip = uiToolTip.ToolTip(250)
		self.toolTip.HideToolTip()

	def SetState(self, progress):
		self.toolTip.ClearToolTip()
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		self.__AppendText("Lv.30 Orkzahne : Stark gegen Monster+10%")
		try:
			self.LoadImage(self.FILE_PATH)
		except:
			print "BiologistAttributeImage.LoadError %s" % (self.FILE_PATH)

		self.SetScale(0.7, 0.7)

	def __AppendText(self, text):
		self.toolTip.AppendTextLine(text)
		self.toolTip.ResizeToolTip()

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()
	
# WEDDING
class LovePointImage(ui.ExpandedImageBox):

	FILE_PATH = "d:/ymir work/ui/pattern/LovePoint/"
	FILE_DICT = {
		0 : FILE_PATH + "01.dds",
		1 : FILE_PATH + "02.dds",
		2 : FILE_PATH + "02.dds",
		3 : FILE_PATH + "03.dds",
		4 : FILE_PATH + "04.dds",
		5 : FILE_PATH + "05.dds",
	}

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		self.loverName = ""
		self.lovePoint = 0

		self.toolTip = uiToolTip.ToolTip(100)
		self.toolTip.HideToolTip()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

	def SetLoverInfo(self, name, lovePoint):
		self.loverName = name
		self.lovePoint = lovePoint
		self.__Refresh()

	def OnUpdateLovePoint(self, lovePoint):
		self.lovePoint = lovePoint
		self.__Refresh()

	def __Refresh(self):
		self.lovePoint = max(0, self.lovePoint)
		self.lovePoint = min(100, self.lovePoint)

		if 0 == self.lovePoint:
			loveGrade = 0
		else:
			loveGrade = self.lovePoint / 25 + 1
		fileName = self.FILE_DICT.get(loveGrade, self.FILE_PATH+"00.dds")

		try:
			self.LoadImage(fileName)
		except:
			import dbg
			dbg.TraceError("LovePointImage.SetLoverInfo(lovePoint=%d) - LoadError %s" % (self.lovePoint, fileName))

		self.SetScale(0.7, 0.7)

		self.toolTip.ClearToolTip()
		self.toolTip.SetTitle(self.loverName)
		self.toolTip.AppendTextLine(localeInfo.AFF_LOVE_POINT % (self.lovePoint))
		self.toolTip.ResizeToolTip()

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()
# END_OF_WEDDING


class HorseImage(ui.ExpandedImageBox):

	FILE_PATH = "d:/ymir work/ui/pattern/HorseState/"

	FILE_DICT = {
		00 : FILE_PATH+"00.dds",
		01 : FILE_PATH+"00.dds",
		02 : FILE_PATH+"00.dds",
		03 : FILE_PATH+"00.dds",
		10 : FILE_PATH+"10.dds",
		11 : FILE_PATH+"11.dds",
		12 : FILE_PATH+"12.dds",
		13 : FILE_PATH+"13.dds",
		20 : FILE_PATH+"20.dds",
		21 : FILE_PATH+"21.dds",
		22 : FILE_PATH+"22.dds",
		23 : FILE_PATH+"23.dds",
		30 : FILE_PATH+"30.dds",
		31 : FILE_PATH+"31.dds",
		32 : FILE_PATH+"32.dds",
		33 : FILE_PATH+"33.dds",
	}

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		#self.textLineList = []
		self.toolTip = uiToolTip.ToolTip(100)
		self.toolTip.HideToolTip()

	def __GetHorseGrade(self, level):
		if 0 == level:
			return 0

		return (level-1)/10 + 1

	def SetState(self, level, health, battery):
		#self.textLineList=[]
		self.toolTip.ClearToolTip()

		if level>0:

			try:
				grade = self.__GetHorseGrade(level)
				self.__AppendText(localeInfo.LEVEL_LIST[grade])
			except IndexError:
				print "HorseImage.SetState(level=%d, health=%d, battery=%d) - Unknown Index" % (level, health, battery)
				return

			try:
				healthName=localeInfo.HEALTH_LIST[health]
				if len(healthName)>0:
					self.__AppendText(healthName)
			except IndexError:
				print "HorseImage.SetState(level=%d, health=%d, battery=%d) - Unknown Index" % (level, health, battery)
				return

			if health>0:
				if battery==0:
					self.__AppendText(localeInfo.NEEFD_REST)

			try:
				fileName=self.FILE_DICT[health*10+battery]
			except KeyError:
				print "HorseImage.SetState(level=%d, health=%d, battery=%d) - KeyError" % (level, health, battery)

			try:
				self.LoadImage(fileName)
			except:
				print "HorseImage.SetState(level=%d, health=%d, battery=%d) - LoadError %s" % (level, health, battery, fileName)

		self.SetScale(0.7, 0.7)

	def __AppendText(self, text):

		self.toolTip.AppendTextLine(text)
		self.toolTip.ResizeToolTip()

		#x=self.GetWidth()/2
		#textLine = ui.TextLine()
		#textLine.SetParent(self)
		#textLine.SetSize(0, 0)
		#textLine.SetOutline()
		#textLine.Hide()
		#textLine.SetPosition(x, 40+len(self.textLineList)*16)
		#textLine.SetText(text)
		#self.textLineList.append(textLine)

	def OnMouseOverIn(self):
		#for textLine in self.textLineList:
		#	textLine.Show()

		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		#for textLine in self.textLineList:
		#	textLine.Hide()

		self.toolTip.HideToolTip()


# AUTO_POTION
class AutoPotionImage(ui.ExpandedImageBox):

	FILE_PATH_HP = "d:/ymir work/ui/pattern/auto_hpgauge/"
	FILE_PATH_SP = "d:/ymir work/ui/pattern/auto_spgauge/"

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		self.loverName = ""
		self.lovePoint = 0
		self.potionType = fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_HP
		self.filePath = ""

		self.toolTip = uiToolTip.ToolTip(100)
		self.toolTip.HideToolTip()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

	def SetPotionType(self, type):
		self.potionType = type
		
		if fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_HP == type:
			self.filePath = self.FILE_PATH_HP
		elif fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_SP == type:
			self.filePath = self.FILE_PATH_SP
			

	def OnUpdateAutoPotionImage(self):
		self.__Refresh()

	def __Refresh(self):
		print "__Refresh"
	
		isActivated, currentAmount, totalAmount, slotIndex = fgGHGjjFHJghjfFG1545gGG.GetAutoPotionInfo(self.potionType)
		
		amountPercent = (float(currentAmount) / totalAmount) * 100.0
		grade = math.ceil(amountPercent / 20)
		
		if 5.0 > amountPercent:
			grade = 0
			
		if 80.0 < amountPercent:
			grade = 4
			if 90.0 < amountPercent:
				grade = 5			

		fmt = self.filePath + "%.2d.dds"
		fileName = fmt % grade
		
		print self.potionType, amountPercent, fileName

		try:
			self.LoadImage(fileName)
		except:
			import dbg
			dbg.TraceError("AutoPotionImage.__Refresh(potionType=%d) - LoadError %s" % (self.potionType, fileName))

		self.SetScale(0.7, 0.7)

		self.toolTip.ClearToolTip()
		
		if fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_HP == type:
			self.toolTip.SetTitle(localeInfo.TOOLTIP_AUTO_POTION_HP)
		else:
			self.toolTip.SetTitle(localeInfo.TOOLTIP_AUTO_POTION_SP)
			
		self.toolTip.AppendTextLine(localeInfo.TOOLTIP_AUTO_POTION_REST	% (amountPercent))
		self.toolTip.ResizeToolTip()

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()
# END_OF_AUTO_POTION


class AffectImage(ui.ExpandedImageBox):

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		self.toolTipText = None
		self.isSkillAffect = TRUE
		self.description = None
		self.endTime = 0
		self.affect = None
		self.isClocked = TRUE

		self.buffQuestionDialog = None
		self.skillIndex = None
		self.SetOnClickEvent(ui.__mem_func__(self.OnBuffQuestionDialog), "MOUSE_LEFT_BUTTON_UP")
		
	def SetAffect(self, affect):
		self.affect = affect

	def GetAffect(self):
		return self.affect

	def SetToolTipText(self, text, x = 0, y = -19):

		if not self.toolTipText:
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetSize(0, 0)
			textLine.SetOutline()
			textLine.Hide()
			self.toolTipText = textLine
			
		self.toolTipText.SetText(text)
		w, h = self.toolTipText.GetTextSize()
		self.toolTipText.SetPosition(max(0, x + self.GetWidth()/2 - w/2), y)

	def SetDescription(self, description):
		self.description = description

	def SetDuration(self, duration):
		self.endTime = 0
		if duration > 0:
			self.endTime = app.GetGlobalTimeStamp() + duration

	def UpdateAutoPotionDescription(self):		
		
		potionType = 0
		if self.affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
			potionType = fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_HP
		else:
			potionType = fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_SP	
		
		isActivated, currentAmount, totalAmount, slotIndex = fgGHGjjFHJghjfFG1545gGG.GetAutoPotionInfo(potionType)
		
		#print "UpdateAutoPotionDescription ", isActivated, currentAmount, totalAmount, slotIndex
		
		amountPercent = 0.0
		
		try:
			amountPercent = (float(currentAmount) / totalAmount) * 100.0		
		except:
			amountPercent = 100.0
		
		self.SetToolTipText(self.description % amountPercent, 0, 40)
		
	def SetClock(self, isClocked):
		self.isClocked = isClocked
		
	def UpdateDescription(self):
		if not self.isClocked:
			self.__UpdateDescription2()
			return
	
		if not self.description:
			return
			
		toolTip = self.description
		if self.endTime > 0:
			leftTime = localeInfo.SecondToDHM(self.endTime - app.GetGlobalTimeStamp())
			toolTip += " (%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
		self.SetToolTipText(toolTip, 0, 40)
		
	#독일버전에서 시간을 제거하기 위해서 사용 
	def __UpdateDescription2(self):
		if not self.description:
			return

		toolTip = self.description
		self.SetToolTipText(toolTip, 0, 40)

	def SetSkillAffectFlag(self, flag):
		self.isSkillAffect = flag

	def SetSkillIndex(self, skillIndex):
		self.skillIndex = skillIndex

	def IsSkillAffect(self):
		return self.isSkillAffect

	def OnMouseOverIn(self):
		if self.toolTipText:
			self.toolTipText.Show()


	def OnMouseOverOut(self):
		if self.toolTipText:
			self.toolTipText.Hide()

	def OnBuffQuestionDialog(self):
		skillIndex = self.skillIndex
		if not skillIndex or skillIndex == 66:
			return
		self.buffQuestionDialog = uiCommon.QuestionDialog()
		self.buffQuestionDialog.SetWidth(350)
		self.buffQuestionDialog.SetText(localeInfo.BUFF_AFFECT_REMOVE_QUESTION % (skill.GetSkillName(skillIndex)))
		self.buffQuestionDialog.SetAcceptEvent(lambda arg = skillIndex: self.OnCloseBuffQuestionDialog(arg))
		self.buffQuestionDialog.SetCancelEvent(lambda arg = 0: self.OnCloseBuffQuestionDialog(arg))
		self.buffQuestionDialog.Open()
			
	def OnCloseBuffQuestionDialog(self, answer):
		if not self.buffQuestionDialog:
			return

		self.buffQuestionDialog.Close()
		self.buffQuestionDialog = None

		if not answer:
			return

		GFHhg54GHGhh45GHGH.SendChatPacket("/remove_buff %d" % answer)
		return TRUE

class AffectShower(ui.Window):

	MALL_DESC_IDX_START = 1000
	IMAGE_STEP = 25
	AFFECT_MAX_NUM = 32

	INFINITE_AFFECT_DURATION = 0x1FFFFFFF 
	
	AFFECT_DATA_DICT =	{
			chr.AFFECT_POISON : (localeInfo.SKILL_TOXICDIE, "d:/ymir work/ui/skill/common/affect/poison.sub"),
			chr.AFFECT_SLOW : (localeInfo.SKILL_SLOW, "d:/ymir work/ui/skill/common/affect/slow.sub"),
			chr.AFFECT_STUN : (localeInfo.SKILL_STUN, "d:/ymir work/ui/skill/common/affect/stun.sub"),

			chr.AFFECT_ATT_SPEED_POTION : (localeInfo.SKILL_INC_ATKSPD, "d:/ymir work/ui/skill/common/affect/Increase_Attack_Speed.sub"),
			chr.AFFECT_MOV_SPEED_POTION : (localeInfo.SKILL_INC_MOVSPD, "d:/ymir work/ui/skill/common/affect/Increase_Move_Speed.sub"),
			chr.AFFECT_FISH_MIND : (localeInfo.SKILL_FISHMIND, "d:/ymir work/ui/skill/common/affect/fishmind.sub"),

			chr.AFFECT_JEONGWI : (localeInfo.SKILL_JEONGWI, "d:/ymir work/ui/skill/warrior/jeongwi_03.sub",),
			chr.AFFECT_GEOMGYEONG : (localeInfo.SKILL_GEOMGYEONG, "d:/ymir work/ui/skill/warrior/geomgyeong_03.sub",),
			chr.AFFECT_CHEONGEUN : (localeInfo.SKILL_CHEONGEUN, "d:/ymir work/ui/skill/warrior/cheongeun_03.sub",),
			chr.AFFECT_GYEONGGONG : (localeInfo.SKILL_GYEONGGONG, "d:/ymir work/ui/skill/assassin/gyeonggong_03.sub",),
			chr.AFFECT_EUNHYEONG : (localeInfo.SKILL_EUNHYEONG, "d:/ymir work/ui/skill/assassin/eunhyeong_03.sub",),
			chr.AFFECT_GWIGEOM : (localeInfo.SKILL_GWIGEOM, "d:/ymir work/ui/skill/sura/gwigeom_03.sub",),
			chr.AFFECT_GONGPO : (localeInfo.SKILL_GONGPO, "d:/ymir work/ui/skill/sura/gongpo_03.sub",),
			chr.AFFECT_JUMAGAP : (localeInfo.SKILL_JUMAGAP, "d:/ymir work/ui/skill/sura/jumagap_03.sub"),
			chr.AFFECT_HOSIN : (localeInfo.SKILL_HOSIN, "d:/ymir work/ui/skill/shaman/hosin_03.sub",),
			chr.AFFECT_BOHO : (localeInfo.SKILL_BOHO, "d:/ymir work/ui/skill/shaman/boho_03.sub",),
			chr.AFFECT_KWAESOK : (localeInfo.SKILL_KWAESOK, "d:/ymir work/ui/skill/shaman/kwaesok_03.sub",),
			chr.AFFECT_HEUKSIN : (localeInfo.SKILL_HEUKSIN, "d:/ymir work/ui/skill/sura/heuksin_03.sub",),
			chr.AFFECT_MUYEONG : (localeInfo.SKILL_MUYEONG, "d:/ymir work/ui/skill/sura/muyeong_03.sub",),
			chr.AFFECT_GICHEON : (localeInfo.SKILL_GICHEON, "d:/ymir work/ui/skill/shaman/gicheon_03.sub",),
			chr.AFFECT_JEUNGRYEOK : (localeInfo.SKILL_JEUNGRYEOK, "d:/ymir work/ui/skill/shaman/jeungryeok_03.sub",),
			chr.AFFECT_PABEOP : (localeInfo.SKILL_PABEOP, "d:/ymir work/ui/skill/sura/pabeop_03.sub",),
			chr.AFFECT_FALLEN_CHEONGEUN : (localeInfo.SKILL_CHEONGEUN, "d:/ymir work/ui/skill/warrior/cheongeun_03.sub",),
			28 : (localeInfo.SKILL_FIRE, "d:/ymir work/ui/skill/sura/hwayeom_03.sub",),
			chr.AFFECT_CHINA_FIREWORK : (localeInfo.SKILL_POWERFUL_STRIKE, "d:/ymir work/ui/skill/common/affect/powerfulstrike.sub",),

			#64 - END
			chr.NEW_AFFECT_EXP_BONUS : (localeInfo.TOOLTIP_MALL_EXPBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/exp_bonus.sub",),

			chr.NEW_AFFECT_ITEM_BONUS : (localeInfo.TOOLTIP_MALL_ITEMBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/item_bonus.sub",),
			chr.NEW_AFFECT_SAFEBOX : (localeInfo.TOOLTIP_MALL_SAFEBOX, "d:/ymir work/ui/skill/common/affect/safebox.sub",),
			chr.NEW_AFFECT_AUTOLOOT : (localeInfo.TOOLTIP_MALL_AUTOLOOT, "d:/ymir work/ui/skill/common/affect/autoloot.sub",),
			chr.NEW_AFFECT_FISH_MIND : (localeInfo.TOOLTIP_MALL_FISH_MIND, "d:/ymir work/ui/skill/common/affect/fishmind.sub",),
			chr.NEW_AFFECT_MARRIAGE_FAST : (localeInfo.TOOLTIP_MALL_MARRIAGE_FAST, "d:/ymir work/ui/skill/common/affect/marriage_fast.sub",),
			chr.NEW_AFFECT_GOLD_BONUS : (localeInfo.TOOLTIP_MALL_GOLDBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/gold_bonus.sub",),

			chr.NEW_AFFECT_NO_DEATH_PENALTY : (localeInfo.TOOLTIP_APPLY_NO_DEATH_PENALTY, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			chr.NEW_AFFECT_SKILL_BOOK_BONUS : (localeInfo.TOOLTIP_APPLY_SKILL_BOOK_BONUS, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			chr.NEW_AFFECT_SKILL_BOOK_NO_DELAY : (localeInfo.TOOLTIP_APPLY_SKILL_BOOK_NO_DELAY, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			
			# 자동물약 hp, sp
			chr.NEW_AFFECT_AUTO_HP_RECOVERY : (localeInfo.TOOLTIP_AUTO_POTION_REST, "d:/ymir work/ui/pattern/auto_hpgauge/05.dds"),			
			chr.NEW_AFFECT_AUTO_SP_RECOVERY : (localeInfo.TOOLTIP_AUTO_POTION_REST, "d:/ymir work/ui/pattern/auto_spgauge/05.dds"),
			#chr.NEW_AFFECT_AUTO_HP_RECOVERY : (localeInfo.TOOLTIP_AUTO_POTION_REST, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),			
			#chr.NEW_AFFECT_AUTO_SP_RECOVERY : (localeInfo.TOOLTIP_AUTO_POTION_REST, "d:/ymir work/ui/skill/common/affect/gold_bonus.sub"),	

			316 : ("Verteidigung+200", "icon/buff/w_tau.tga",), # W Tau PERMA
			317 : ("Angriffswer+120", "icon/buff/blauer_tau.tga",), # Blau Tau PERMA
			318 : ("Durchb. Trefferchance+20%", "icon/buff/roter_tau.tga",), # Roter Tau PERMA
			319 : ("Angriffswert+20%", "icon/buff/drachengott_angriff.tga",), # Drachengott Angriff PERMA
			320 : ("Verteidigung+20%", "icon/buff/drachengott_verteidigung.tga",), # Drachengott Verteidigung PERMA
			321 : ("Max. TP+20%", "icon/buff/drachengott_leben.tga",), # Drachengott Leben PERMA
			322 : ("Krit. Trefferchance+20%", "icon/buff/krit_kampf.tga",), # Krit Kampf PERMA
			323 : ("Durchb. Trefferchance+20%", "icon/buff/db_kampf.tga",), # DB Kampf PERMA
			
			324 : ("Angriffswer+120", "icon/buff/roter_tau_n.tga",), # Roter Tau NORMAL
			325 : ("Durchb. Trefferchance+20%", "icon/buff/blauer_tau_n.tga",), # Blau Tau NORMAL
			326 : ("Max. TP+20%", "icon/buff/drachengott_leben_n.tga",), # Drachengott Leben NORMAL
			327 : ("Verteidigung+20%", "icon/buff/drachengott_verteidigung_n.tga",), # Drachengott Verteidigung NORMAL
			328 : ("Angriffswert+20%", "icon/buff/drachengott_angriff_n.tga",), # Drachengott Angriff NORMAL
			329 : ("Krit. Trefferchance+20%", "icon/buff/krit_kampf_n.tga",), # Krit Kampf NORMAL
			330 : ("Durchb. Trefferchance+20%", "icon/buff/db_kampf_n.tga",), # DB Kampf NORMAL			
			

			900 : ("Du erhalst zurzeit keine Erfahrungspunkte!", "affect_icons_wod/wod_no_exp.tga",),
			901 : ("Der Yang-Chat wurde ausgeblendet.", "affect_icons_wod/no_yang_chat.tga",),
			902 : ("Haustier", "affect_icons_wod/pet_summon.tga",),
			903 : ("Tranke werden automatisch reaktiviert.", "affect_icons_wod/no_yang_chat.tga",),
			904 : ("Dein Pet erhalt zurzeit doppelte EXP.", "affect_icons_wod/pet_exp.tga",),
			905 : ("Du hast dein Pet gerufen!", "affect_icons_wod/pet_summon.tga",),
			906 : ("Dein Pet sammelt alles auf!", "affect_icons_wod/pet_pickup.tga",),

			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MALL_ATTBONUS : (localeInfo.TOOLTIP_MALL_ATTBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/att_bonus.sub",),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MALL_DEFBONUS : (localeInfo.TOOLTIP_MALL_DEFBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/def_bonus.sub",),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MALL_EXPBONUS : (localeInfo.TOOLTIP_MALL_EXPBONUS, "d:/ymir work/ui/skill/common/affect/exp_bonus.sub",),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MALL_ITEMBONUS : (localeInfo.TOOLTIP_MALL_ITEMBONUS, "d:/ymir work/ui/skill/common/affect/item_bonus.sub",),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MALL_GOLDBONUS : (localeInfo.TOOLTIP_MALL_GOLDBONUS, "d:/ymir work/ui/skill/common/affect/gold_bonus.sub",),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_CRITICAL_PCT : (localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,"d:/ymir work/ui/skill/common/affect/critical.sub"),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_PENETRATE_PCT : (localeInfo.TOOLTIP_APPLY_PENETRATE_PCT, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MAX_HP_PCT : (localeInfo.TOOLTIP_MAX_HP_PCT, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_MAX_SP_PCT : (localeInfo.TOOLTIP_MAX_SP_PCT, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),	

			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_PC_BANG_EXP_BONUS : (localeInfo.TOOLTIP_MALL_EXPBONUS_P_STATIC, "d:/ymir work/ui/skill/common/affect/EXP_Bonus_p_on.sub",),
			MALL_DESC_IDX_START+fgGHGjjFHJghjfFG1545gGG.POINT_PC_BANG_DROP_BONUS: (localeInfo.TOOLTIP_MALL_ITEMBONUS_P_STATIC, "d:/ymir work/ui/skill/common/affect/Item_Bonus_p_on.sub",),
	}
	if app.ENABLE_DRAGON_SOUL_SYSTEM:
		# 용혼석 천, 지 덱.
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK1] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK1, "d:/ymir work/ui/dragonsoul/buff_ds_sky1.tga")
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK2] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK2, "d:/ymir work/ui/dragonsoul/buff_ds_land1.tga")
		
	if app.ENABLE_NEW_AFFECT_POTION:	
		AFFECT_DATA_DICT[AFFECT_POTION["affect"][0]] = (localeInfo.TOOLTIP_AFFECT_POTION_1, AFFECT_POTION["image"][0])
		AFFECT_DATA_DICT[AFFECT_POTION["affect"][1]] = (localeInfo.TOOLTIP_AFFECT_POTION_2, AFFECT_POTION["image"][1])
		AFFECT_DATA_DICT[AFFECT_POTION["affect"][2]] = (localeInfo.TOOLTIP_AFFECT_POTION_3, AFFECT_POTION["image"][2])
		AFFECT_DATA_DICT[AFFECT_POTION["affect"][3]] = (localeInfo.TOOLTIP_AFFECT_POTION_4, AFFECT_POTION["image"][3])
		AFFECT_DATA_DICT[AFFECT_POTION["affect"][4]] = (localeInfo.TOOLTIP_AFFECT_POTION_5, AFFECT_POTION["image"][4])
		AFFECT_DATA_DICT[AFFECT_POTION["affect"][5]] = (localeInfo.TOOLTIP_AFFECT_POTION_6, AFFECT_POTION["image"][5])

	def __init__(self):
		ui.Window.__init__(self)

		self.serverPlayTime=0
		self.clientPlayTime=0
		
		self.lastUpdateTime=0
		self.affectImageDict={}
		self.horseImage=None
		self.lovePointImage=None
		self.biologistImage=None
		self.autoPotionImageHP = AutoPotionImage()
		self.autoPotionImageSP = AutoPotionImage()
		self.SetPosition(10, 10)
		self.Show()

	def ClearAllAffects(self):
		self.horseImage=None
		self.lovePointImage=None
		self.biologistImage=None
		self.affectImageDict={}
		self.__ArrangeImageList()

	def ClearAffects(self): ## 스킬 이펙트만 없앱니다.
		self.living_affectImageDict={}
		for key, image in self.affectImageDict.items():
			if not image.IsSkillAffect():
				self.living_affectImageDict[key] = image
		self.affectImageDict = self.living_affectImageDict
		self.__ArrangeImageList()

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		
		if self.IS_PERMA_POTION_AFFECT(type):
			self.SetAffect(type)
			return
			
		if self.IS_NORMAL_POTION_AFFECT(type):
			self.SetAffect(type)
			return
			
		print "BINARY_NEW_AddAffect", type, pointIdx, value, duration

		if app.ENABLE_NEW_AFFECT_POTION:
			if type < 500 and not type == AFFECT_POTION["affect"][0] and not type == AFFECT_POTION["affect"][1] and not type == AFFECT_POTION["affect"][2] and not type == AFFECT_POTION["affect"][3] and not type == AFFECT_POTION["affect"][4] and not type == AFFECT_POTION["affect"][5]:
				if not self.IS_PERMA_POTION_AFFECT(type):
					if not self.IS_NORMAL_POTION_AFFECT(type):
						return
		else:
			if type < 500:
				return	

		if type == chr.NEW_AFFECT_MALL:
			affect = self.MALL_DESC_IDX_START + pointIdx
		else:
			affect = type

		if self.affectImageDict.has_key(affect):
			return

		if not self.AFFECT_DATA_DICT.has_key(affect):
			return

		## 용신의 가호, 선인의 교훈은 Duration 을 0 으로 설정한다.
		if affect == chr.NEW_AFFECT_NO_DEATH_PENALTY or\
		   affect == chr.NEW_AFFECT_SKILL_BOOK_BONUS or\
		   affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or\
		   affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY or\
		   affect == chr.NEW_AFFECT_SKILL_BOOK_NO_DELAY:
			duration = 0

		affectData = self.AFFECT_DATA_DICT[affect]
		description = affectData[0]
		filename = affectData[1]
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "test 1")
		if pointIdx == fgGHGjjFHJghjfFG1545gGG.POINT_MALL_ITEMBONUS or\
		   pointIdx == fgGHGjjFHJghjfFG1545gGG.POINT_MALL_GOLDBONUS:
			value = 1 + float(value) / 100.0

		trashValue = 123
		#if affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
		if trashValue == 1:
			try:
				#image = AutoPotionImage()
				#image.SetParent(self)
				image = None
				
				if affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
					image.SetPotionType(fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_SP)
					image = self.autoPotionImageSP
					#self.autoPotionImageSP = image;
				else:
					image.SetPotionType(fgGHGjjFHJghjfFG1545gGG.AUTO_POTION_TYPE_HP)
					image = self.autoPotionImageHP
					#self.autoPotionImageHP = image;
				
				image.SetParent(self)
				image.Show()
				image.OnUpdateAutoPotionImage()
				
				self.affectImageDict[affect] = image
				self.__ArrangeImageList()
				
			except Exception, e:
				print "except Aff auto potion affect ", e
				pass				
			
		else:
			if affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY:
				description = description(float(value))

			try:
				print "Add affect %s" % affect
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"  Add affect " + str(affect))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"  description " + str(description))
				image = AffectImage()
				image.SetParent(self)
				image.LoadImage(filename)
				image.SetDescription(description)
				image.SetDuration(duration)
				image.SetAffect(affect)
				if affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE or\
					affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15 or\
					self.INFINITE_AFFECT_DURATION < duration:
					image.SetClock(FALSE)
					image.UpdateDescription()
				elif affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
					image.UpdateAutoPotionDescription()
				else:
					image.UpdateDescription()
					
				if affect == chr.NEW_AFFECT_DRAGON_SOUL_DECK1 or affect == chr.NEW_AFFECT_DRAGON_SOUL_DECK2:
					image.SetScale(1, 1)
				else:
					image.SetScale(0.7, 0.7)
				image.SetSkillAffectFlag(FALSE)
				image.Show()
				self.affectImageDict[affect] = image
				self.__ArrangeImageList()
			except Exception, e:
				print "except Aff affect ", e
				pass

	def BINARY_NEW_RemoveAffect(self, type, pointIdx):

		if self.IS_PERMA_POTION_AFFECT(type):
			self.ResetAffect(type)
			return

		if self.IS_NORMAL_POTION_AFFECT(type):
			self.ResetAffect(type)
			return
	
		if type == chr.NEW_AFFECT_MALL:
			affect = self.MALL_DESC_IDX_START + pointIdx
		else:
			affect = type
	
		print "Remove Affect %s %s" % ( type , pointIdx )
		self.__RemoveAffect(affect)
		self.__ArrangeImageList()
	
	def IS_PERMA_POTION_AFFECT(self,type):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "IS_PERMA_AFFECT: " + str(type))
		if type >= 316 and type <= 323:
			return True
		else:
			return False
			
	def IS_NORMAL_POTION_AFFECT(self,type):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "IS_PERMA_AFFECT: " + str(type))
		if type >= 324 and type <= 330:
			return True
		else:
			return False
	
	def SetAffect(self, affect):
		self.__AppendAffect(affect)
		self.__ArrangeImageList()

	def ResetAffect(self, affect):
		self.__RemoveAffect(affect)
		self.__ArrangeImageList()

	def SetLoverInfo(self, name, lovePoint):
		image = LovePointImage()
		image.SetParent(self)
		image.SetLoverInfo(name, lovePoint)
		self.lovePointImage = image
		self.__ArrangeImageList()

	def ShowLoverState(self):
		if self.lovePointImage:
			self.lovePointImage.Show()
			self.__ArrangeImageList()

	def HideLoverState(self):
		if self.lovePointImage:
			self.lovePointImage.Hide()
			self.__ArrangeImageList()

	def ClearLoverState(self):
		self.lovePointImage = None
		self.__ArrangeImageList()

	def OnUpdateLovePoint(self, lovePoint):
		if self.lovePointImage:
			self.lovePointImage.OnUpdateLovePoint(lovePoint)

	def SetHorseState(self, level, health, battery):
		if level==0:
			self.horseImage=None
		else:
			image = HorseImage()
			image.SetParent(self)
			image.SetState(level, health, battery)
			image.Show()

			self.horseImage=image
			self.__ArrangeImageList()
			
	def SetBiologistState(self,progress):
		if progress==0:
			self.biologistImage=None
		else:
			image = BiologistAttributeImage()
			image.SetParent(self)
			image.SetState(progress)
			image.Show()

			self.biologistImage=image
			self.__ArrangeImageList()	

	def SetPlayTime(self, playTime):
		self.serverPlayTime = playTime
		self.clientPlayTime = app.GetTime()
		
		if localeInfo.IsVIETNAM():		
			image = PlayTimeImage()
			image.SetParent(self)
			image.SetPlayTime(playTime)
			image.Show()

			self.playTimeImage=image
			self.__ArrangeImageList()

	def __AppendAffect(self, affect):

		if self.affectImageDict.has_key(affect):
			return

		try:
			affectData = self.AFFECT_DATA_DICT[affect]
		except KeyError:
			return

		name = affectData[0]
		filename = affectData[1]

		skillIndex = fgGHGjjFHJghjfFG1545gGG.AffectIndexToSkillIndex(affect)
		if 0 != skillIndex:
			name = skill.GetSkillName(skillIndex)

		image = AffectImage()
		image.SetParent(self)
		image.SetSkillAffectFlag(TRUE)
		image.SetSkillIndex(skillIndex)
		
		try:
			image.LoadImage(filename)
		except:
			pass

		image.SetToolTipText(name, 0, 40)
		image.SetScale(0.7, 0.7)
		image.Show()
		self.affectImageDict[affect] = image

	def __RemoveAffect(self, affect):
		"""
		if affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
			self.autoPotionImageSP.Hide()

		if affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
			self.autoPotionImageHP.Hide()
		"""
			
		if not self.affectImageDict.has_key(affect):
			print "__RemoveAffect %s ( No Affect )" % affect
			return

		print "__RemoveAffect %s ( Affect )" % affect
		del self.affectImageDict[affect]
		
		self.__ArrangeImageList()

	def __ArrangeImageList(self):

		width = len(self.affectImageDict) * self.IMAGE_STEP
		if self.lovePointImage:
			width+=self.IMAGE_STEP
		if self.horseImage:
			width+=self.IMAGE_STEP

		self.SetSize(width, 26)

		xPos = 0

		if self.lovePointImage:
			if self.lovePointImage.IsShow():
				self.lovePointImage.SetPosition(xPos, 0)
				xPos += self.IMAGE_STEP

		if self.horseImage:
			self.horseImage.SetPosition(xPos, 0)
			xPos += self.IMAGE_STEP
			
		if self.biologistImage:
			self.biologistImage.SetPosition(xPos, 0)
			xPos += self.IMAGE_STEP
			
		for image in self.affectImageDict.values():
			image.SetPosition(xPos, 0)
			xPos += self.IMAGE_STEP

	def ShowPetAffect(self,status):
		if status == 1:
			self.SetAffect(902)
		else:
			self.ResetAffect(902)
			
	def ShowAutoPotAffect(self,status):
		if status == 1:
			self.SetAffect(903)
		else:
			self.ResetAffect(903)		

	def OnUpdate(self):		
		try:
			if app.GetGlobalTime() - self.lastUpdateTime > 500:
			#if 0 < app.GetGlobalTime():
				self.lastUpdateTime = app.GetGlobalTime()

				for image in self.affectImageDict.values():
					if image.GetAffect() == chr.NEW_AFFECT_AUTO_HP_RECOVERY or image.GetAffect() == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
						image.UpdateAutoPotionDescription()
						continue
						
					if not image.IsSkillAffect():
						image.UpdateDescription()
		except Exception, e:
			print "AffectShower::OnUpdate error : ", e

		if constInfo.AntiExpStatus == 1:
			self.SetAffect(900)
		else:
			self.ResetAffect(900)
			
		if constInfo.YangChatStatus == 1:
			self.SetAffect(901)
		else:
			self.ResetAffect(901)
			
		# if constInfo.PET_INFOS["double_exp"] > app.GetGlobalTimeStamp():
			# self.SetAffect(904)
		# else:
			# self.ResetAffect(904)			
			
		# if constInfo.PET_INFOS["level"] > 0:
			# self.SetAffect(905)
		# else:
			# self.ResetAffect(905)				

		# if constInfo.PET_INFOS["skill_status"] == 1:
			# self.SetAffect(906)
		# else:
			# self.ResetAffect(906)	
			