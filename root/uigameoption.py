import ui
import snd
import systemSetting
import GFHhg54GHGhh45GHGH
import chat
import app
import localeInfo
import constInfo
import chrmgr
import fgGHGjjFHJghjfFG1545gGG
import uiPrivateShopBuilder # ����ȣ
import interfaceModule # ����ȣ
import background

blockMode = 0
viewChatMode = 0

MOBILE = FALSE

if localeInfo.IsYMIR():
	MOBILE = TRUE


class OptionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()
		self.RefreshViewChat()
		self.RefreshAlwaysShowName()
		self.RefreshShowDamage()
		self.RefreshShowSalesText()
		self.RefreshShowNightText()
		if app.WJ_SHOW_MOB_INFO:
			self.RefreshShowMobInfo()
		self.RefreshHideCostume()
		self.RefreshHideCostume2()
		self.RefreshMultiShopLock()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE GAME OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0
		self.nameColorModeButtonList = []
		self.viewTargetBoardButtonList = []
		self.pvpModeButtonDict = {}
		self.blockButtonList = []
		self.viewChatButtonList = []
		self.alwaysShowNameButtonList = []
		self.showDamageButtonList = []
		self.showsalesTextButtonList = []
		if app.WJ_SHOW_MOB_INFO:
			self.showMobInfoButtonList = []
		self.showNightButtonList = []
		self.showHideCostumeButtonList = []
		self.showHideCostumeButtonList2 = []
		self.bindMultiShopButton = []

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY GAME OPTION DIALOG"
	
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.nameColorModeButtonList.append(GetObject("name_color_normal"))
			self.nameColorModeButtonList.append(GetObject("name_color_empire"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_no_view"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_view"))
			self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_PEACE] = GetObject("pvp_peace")
			self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_REVENGE] = GetObject("pvp_revenge")
			self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_GUILD] = GetObject("pvp_guild")
			self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_FREE] = GetObject("pvp_free")
			self.blockButtonList.append(GetObject("block_exchange_button"))
			self.blockButtonList.append(GetObject("block_party_button"))
			self.blockButtonList.append(GetObject("block_guild_button"))
			self.blockButtonList.append(GetObject("block_whisper_button"))
			self.blockButtonList.append(GetObject("block_friend_button"))
			self.blockButtonList.append(GetObject("block_party_request_button"))
			self.viewChatButtonList.append(GetObject("view_chat_on_button"))
			self.viewChatButtonList.append(GetObject("view_chat_off_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_on_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_off_button"))
			self.showDamageButtonList.append(GetObject("show_damage_on_button"))
			self.showDamageButtonList.append(GetObject("show_damage_off_button"))
			self.showsalesTextButtonList.append(GetObject("salestext_on_button"))
			self.showsalesTextButtonList.append(GetObject("salestext_off_button"))
			
			if app.WJ_SHOW_MOB_INFO:
				self.showMobInfoButtonList.append(GetObject("show_mob_level_button"))
				self.showMobInfoButtonList.append(GetObject("show_mob_AI_flag_button"))
			
			self.showNightButtonList.append(GetObject("showNight_on_button"))
			self.showNightButtonList.append(GetObject("showNight_off_button"))

			self.showHideCostumeButtonList.append(GetObject("costumeHide_hide_button"))
			self.showHideCostumeButtonList.append(GetObject("costumeHide_show_button"))
			
			self.showHideCostumeButtonList2.append(GetObject("costumeHide_hide_button2"))
			self.showHideCostumeButtonList2.append(GetObject("costumeHide_show_button2"))

			self.bindMultiShopButton.append(GetObject("bindMultiShop_RadioButton_Bind"))
			self.bindMultiShopButton.append(GetObject("bindMultiShop_RadioButton_UnBind"))
			
			global MOBILE
			if MOBILE:
				self.inputMobileButton = GetObject("input_mobile_button")
				self.deleteMobileButton = GetObject("delete_mobile_button")


		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		global MOBILE
		if MOBILE:
			self.__Load_LoadScript("uiscript/gameoptiondialog_formobile.py")
		else:
			self.__Load_LoadScript("uiscript/gameoptiondialog.py")

		self.__Load_BindObject()

		self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.nameColorModeButtonList[0].SAFE_SetEvent(self.__OnClickNameColorModeNormalButton)
		self.nameColorModeButtonList[1].SAFE_SetEvent(self.__OnClickNameColorModeEmpireButton)

		self.viewTargetBoardButtonList[0].SAFE_SetEvent(self.__OnClickTargetBoardViewButton)
		self.viewTargetBoardButtonList[1].SAFE_SetEvent(self.__OnClickTargetBoardNoViewButton)

		self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_PEACE].SAFE_SetEvent(self.__OnClickPvPModePeaceButton)
		self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_REVENGE].SAFE_SetEvent(self.__OnClickPvPModeRevengeButton)
		self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_GUILD].SAFE_SetEvent(self.__OnClickPvPModeGuildButton)
		self.pvpModeButtonDict[fgGHGjjFHJghjfFG1545gGG.PK_MODE_FREE].SAFE_SetEvent(self.__OnClickPvPModeFreeButton)

		self.blockButtonList[0].SetToggleUpEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleUpEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleUpEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleUpEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleUpEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleUpEvent(self.__OnClickBlockPartyRequest)

		self.blockButtonList[0].SetToggleDownEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleDownEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleDownEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleDownEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleDownEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleDownEvent(self.__OnClickBlockPartyRequest)

		self.viewChatButtonList[0].SAFE_SetEvent(self.__OnClickViewChatOnButton)
		self.viewChatButtonList[1].SAFE_SetEvent(self.__OnClickViewChatOffButton)

		self.alwaysShowNameButtonList[0].SAFE_SetEvent(self.__OnClickAlwaysShowNameOnButton)
		self.alwaysShowNameButtonList[1].SAFE_SetEvent(self.__OnClickAlwaysShowNameOffButton)

		self.showDamageButtonList[0].SAFE_SetEvent(self.__OnClickShowDamageOnButton)
		self.showDamageButtonList[1].SAFE_SetEvent(self.__OnClickShowDamageOffButton)
		
		self.showsalesTextButtonList[0].SAFE_SetEvent(self.__OnClickSalesTextOnButton)
		self.showsalesTextButtonList[1].SAFE_SetEvent(self.__OnClickSalesTextOffButton)		
		
		if app.WJ_SHOW_MOB_INFO:
			self.showMobInfoButtonList[0].SetToggleUpEvent(self.__OnClickShowMobLevelButton)
			self.showMobInfoButtonList[1].SetToggleUpEvent(self.__OnClickShowMobAIFlagButton)

			self.showMobInfoButtonList[0].SetToggleDownEvent(self.__OnClickShowMobLevelButton)
			self.showMobInfoButtonList[1].SetToggleDownEvent(self.__OnClickShowMobAIFlagButton)
		
		self.showNightButtonList[0].SAFE_SetEvent(self.__OnClickShowNightOnButton)
		self.showNightButtonList[1].SAFE_SetEvent(self.__OnClickShowNightOffButton)
		
		self.showHideCostumeButtonList[0].SAFE_SetEvent(self.__OnClickHideCostumeButton)
		self.showHideCostumeButtonList[1].SAFE_SetEvent(self.__OnClickShowCostumeButton)
		
		self.showHideCostumeButtonList2[0].SAFE_SetEvent(self.__OnClickHideCostumeButton2)
		self.showHideCostumeButtonList2[1].SAFE_SetEvent(self.__OnClickShowCostumeButton2)
		
		self.bindMultiShopButton[0].SAFE_SetEvent(self.__OnClickBindMultiShopButton)
		self.bindMultiShopButton[1].SAFE_SetEvent(self.__OnClickBindMultiShopButton)

		self.__ClickRadioButton(self.nameColorModeButtonList, constInfo.GET_CHRNAME_COLOR_INDEX())
		self.__ClickRadioButton(self.viewTargetBoardButtonList, constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())
		self.__SetPeacePKMode()

		#global MOBILE
		if MOBILE:
			self.inputMobileButton.SetEvent(ui.__mem_func__(self.__OnChangeMobilePhoneNumber))
			self.deleteMobileButton.SetEvent(ui.__mem_func__(self.__OnDeleteMobilePhoneNumber))

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def __SetNameColorMode(self, index):
		constInfo.SET_CHRNAME_COLOR_INDEX(index)
		self.__ClickRadioButton(self.nameColorModeButtonList, index)

	def __SetTargetBoardViewMode(self, flag):
		constInfo.SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(flag)
		self.__ClickRadioButton(self.viewTargetBoardButtonList, flag)

	def __OnClickNameColorModeNormalButton(self):
		self.__SetNameColorMode(0)

	def __OnClickNameColorModeEmpireButton(self):
		self.__SetNameColorMode(1)

	def __OnClickTargetBoardViewButton(self):
		self.__SetTargetBoardViewMode(0)

	def __OnClickTargetBoardNoViewButton(self):
		self.__SetTargetBoardViewMode(1)

	def __OnClickCameraModeShortButton(self):
		self.__SetCameraMode(0)

	def __OnClickCameraModeLongButton(self):
		self.__SetCameraMode(1)

	def __OnClickFogModeLevel0Button(self):
		self.__SetFogLevel(0)

	def __OnClickFogModeLevel1Button(self):
		self.__SetFogLevel(1)

	def __OnClickFogModeLevel2Button(self):
		self.__SetFogLevel(2)

	def __OnClickBlockExchangeButton(self):
		self.RefreshBlock()
		global blockMode
		GFHhg54GHGhh45GHGH.SendChatPacket("/setblockmode " + str(blockMode ^ fgGHGjjFHJghjfFG1545gGG.BLOCK_EXCHANGE))
	def __OnClickBlockPartyButton(self):
		self.RefreshBlock()
		global blockMode
		GFHhg54GHGhh45GHGH.SendChatPacket("/setblockmode " + str(blockMode ^ fgGHGjjFHJghjfFG1545gGG.BLOCK_PARTY))
	def __OnClickBlockGuildButton(self):
		self.RefreshBlock()
		global blockMode
		GFHhg54GHGhh45GHGH.SendChatPacket("/setblockmode " + str(blockMode ^ fgGHGjjFHJghjfFG1545gGG.BLOCK_GUILD))
	def __OnClickBlockWhisperButton(self):
		self.RefreshBlock()
		global blockMode
		GFHhg54GHGhh45GHGH.SendChatPacket("/setblockmode " + str(blockMode ^ fgGHGjjFHJghjfFG1545gGG.BLOCK_WHISPER))
	def __OnClickBlockFriendButton(self):
		self.RefreshBlock()
		global blockMode
		GFHhg54GHGhh45GHGH.SendChatPacket("/setblockmode " + str(blockMode ^ fgGHGjjFHJghjfFG1545gGG.BLOCK_FRIEND))
	def __OnClickBlockPartyRequest(self):
		self.RefreshBlock()
		global blockMode
		GFHhg54GHGhh45GHGH.SendChatPacket("/setblockmode " + str(blockMode ^ fgGHGjjFHJghjfFG1545gGG.BLOCK_PARTY_REQUEST))

	def __OnClickViewChatOnButton(self):
		global viewChatMode
		viewChatMode = 1
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()
	def __OnClickViewChatOffButton(self):
		global viewChatMode
		viewChatMode = 0
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()

	def __OnClickAlwaysShowNameOnButton(self):
		systemSetting.SetAlwaysShowNameFlag(True)
		self.RefreshAlwaysShowName()

	def __OnClickAlwaysShowNameOffButton(self):
		systemSetting.SetAlwaysShowNameFlag(False)
		self.RefreshAlwaysShowName()

	def __OnClickShowDamageOnButton(self):
		systemSetting.SetShowDamageFlag(True)
		self.RefreshShowDamage()

	def __OnClickShowDamageOffButton(self):
		systemSetting.SetShowDamageFlag(False)
		self.RefreshShowDamage()
		
	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(True)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()
		
	def __OnClickSalesTextOffButton(self):
		systemSetting.SetShowSalesTextFlag(False)
		self.RefreshShowSalesText()
		
	def __OnClickShowMobLevelButton(self):
		if app.WJ_SHOW_MOB_INFO:
			if systemSetting.IsShowMobLevel():
				systemSetting.SetShowMobLevel(False)
			else:
				systemSetting.SetShowMobLevel(True)

			self.RefreshShowMobInfo()

	def __OnClickShowMobAIFlagButton(self):
		if app.WJ_SHOW_MOB_INFO:
			if systemSetting.IsShowMobAIFlag():
				systemSetting.SetShowMobAIFlag(False)
			else:
				systemSetting.SetShowMobAIFlag(True)

			self.RefreshShowMobInfo()
		
	def __OnClickShowNightOnButton(self):
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(1)
		constInfo.Night = 1
		self.RefreshShowNightText()	

	def __OnClickShowNightOffButton(self):
		background.SetEnvironmentData(0)
		constInfo.Night = 0
		self.RefreshShowNightText()
		
	def __OnClickHideCostumeButton(self):
		if constInfo.HideCostume == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Dein R�stungskost�m wird nun ausgeblendet!")
			constInfo.HideCostume  = 1
			GFHhg54GHGhh45GHGH.SendChatPacket("/costvisible 0")
			self.RefreshHideCostume()
			
	def __OnClickShowCostumeButton(self):
		if constInfo.HideCostume == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Dein R�stungskost�m wird nun angezeigt!")
			constInfo.HideCostume  = 0
			GFHhg54GHGhh45GHGH.SendChatPacket("/costvisible 0")
			self.RefreshHideCostume()
			
	def __OnClickHideCostumeButton2(self):
		if constInfo.HideCostume2 == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Dein Waffenkost�m wird nun ausgeblendet!")
			constInfo.HideCostume2  = 1
			GFHhg54GHGhh45GHGH.SendChatPacket("/costvisible 1")
			self.RefreshHideCostume2()
			
	def __OnClickShowCostumeButton2(self):
		if constInfo.HideCostume2 == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Dein Waffenkost�m wird nun angezeigt!")
			constInfo.HideCostume2  = 0
			GFHhg54GHGhh45GHGH.SendChatPacket("/costvisible 1")
			self.RefreshHideCostume2()
			
			
	def __OnClickBindMultiShopButton(self):
		if systemSetting.IsMultiShopLock() == 0:
			systemSetting.SetMutliShopLock(1)
		else:
			systemSetting.SetMutliShopLock(0)
			
		self.RefreshMultiShopLock()
		
		
		
	def __CheckPvPProtectedLevelPlayer(self):	
		if fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__SetPeacePKMode()
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1

		return 0

	def __SetPKMode(self, mode):
		for btn in self.pvpModeButtonDict.values():
			btn.SetUp()
		if self.pvpModeButtonDict.has_key(mode):
			self.pvpModeButtonDict[mode].Down()

	def __SetPeacePKMode(self):
		self.__SetPKMode(fgGHGjjFHJghjfFG1545gGG.PK_MODE_PEACE)

	def __RefreshPVPButtonList(self):
		self.__SetPKMode(fgGHGjjFHJghjfFG1545gGG.GetPKMode())

	def __OnClickPvPModePeaceButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			GFHhg54GHGhh45GHGH.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeRevengeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			GFHhg54GHGhh45GHGH.SendChatPacket("/pkmode 1", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeFreeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			GFHhg54GHGhh45GHGH.SendChatPacket("/pkmode 2", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeGuildButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if 0 == fgGHGjjFHJghjfFG1545gGG.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			GFHhg54GHGhh45GHGH.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def OnChangePKMode(self):
		self.__RefreshPVPButtonList()

	def __OnChangeMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_TITLE)
		inputDialog.SetMaxLength(13)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobilePhoneNumber))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog

	def __OnDeleteMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.MESSENGER_DO_YOU_DELETE_PHONE_NUMBER)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDeleteMobile))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

	def OnInputMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		text.replace('-', '')
		GFHhg54GHGhh45GHGH.SendChatPacket("/mobile " + text)
		self.OnCloseInputDialog()
		return True

	def OnInputMobileAuthorityCode(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()
		GFHhg54GHGhh45GHGH.SendChatPacket("/mobile_auth " + text)
		self.OnCloseInputDialog()
		return True

	def OnDeleteMobile(self):
		global MOBILE
		if not MOBILE:
			return

		GFHhg54GHGhh45GHGH.SendChatPacket("/mobile")
		self.OnCloseQuestionDialog()
		return True

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def RefreshMobile(self):
		global MOBILE
		if not MOBILE:
			return

		if fgGHGjjFHJghjfFG1545gGG.HasMobilePhoneNumber():
			self.inputMobileButton.Hide()
			self.deleteMobileButton.Show()
		else:
			self.inputMobileButton.Show()
			self.deleteMobileButton.Hide()

	def OnMobileAuthority(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialogWithDescription()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_TITLE)
		inputDialog.SetDescription(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_DESCRIPTION)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobileAuthorityCode))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.SetMaxLength(4)
		inputDialog.SetBoardWidth(310)
		inputDialog.Open()
		self.inputDialog = inputDialog

	def RefreshBlock(self):
		global blockMode
		for i in xrange(len(self.blockButtonList)):
			if 0 != (blockMode & (1 << i)):
				self.blockButtonList[i].Down()
			else:
				self.blockButtonList[i].SetUp()

	def RefreshViewChat(self):
		if systemSetting.IsViewChat():
			self.viewChatButtonList[0].Down()
			self.viewChatButtonList[1].SetUp()
		else:
			self.viewChatButtonList[0].SetUp()
			self.viewChatButtonList[1].Down()

	def RefreshAlwaysShowName(self):
		if systemSetting.IsAlwaysShowName():
			self.alwaysShowNameButtonList[0].Down()
			self.alwaysShowNameButtonList[1].SetUp()
		else:
			self.alwaysShowNameButtonList[0].SetUp()
			self.alwaysShowNameButtonList[1].Down()

	def RefreshShowDamage(self):
		if systemSetting.IsShowDamage():
			self.showDamageButtonList[0].Down()
			self.showDamageButtonList[1].SetUp()
		else:
			self.showDamageButtonList[0].SetUp()
			self.showDamageButtonList[1].Down()
			
	def RefreshShowSalesText(self):
		if systemSetting.IsShowSalesText():
			self.showsalesTextButtonList[0].Down()
			self.showsalesTextButtonList[1].SetUp()
		else:
			self.showsalesTextButtonList[0].SetUp()
			self.showsalesTextButtonList[1].Down()
			
	def RefreshShowMobInfo(self):
		if app.WJ_SHOW_MOB_INFO:
			if systemSetting.IsShowMobLevel():
				self.showMobInfoButtonList[0].Down()
			else:
				self.showMobInfoButtonList[0].SetUp()

			if systemSetting.IsShowMobAIFlag():
				self.showMobInfoButtonList[1].Down()
			else:
				self.showMobInfoButtonList[1].SetUp()
			
	def RefreshShowNightText(self):
		if constInfo.Night == 1:
			self.showNightButtonList[0].Down()
			self.showNightButtonList[1].SetUp()
		else:
			self.showNightButtonList[0].SetUp()
			self.showNightButtonList[1].Down()
			
	def RefreshHideCostume(self):
		if constInfo.HideCostume == 1:
			self.showHideCostumeButtonList[0].Down()
			self.showHideCostumeButtonList[1].SetUp()
		else:
			self.showHideCostumeButtonList[0].SetUp()
			self.showHideCostumeButtonList[1].Down()
			
	def RefreshHideCostume2(self):
		if constInfo.HideCostume2 == 1:
			self.showHideCostumeButtonList2[0].Down()
			self.showHideCostumeButtonList2[1].SetUp()
		else:
			self.showHideCostumeButtonList2[0].SetUp()
			self.showHideCostumeButtonList2[1].Down()
			
	def RefreshMultiShopLock(self):
		if systemSetting.IsMultiShopLock() == 1:
			self.bindMultiShopButton[0].Down()
			self.bindMultiShopButton[1].SetUp()			
		elif systemSetting.IsMultiShopLock() == 0:
			self.bindMultiShopButton[0].SetUp()
			self.bindMultiShopButton[1].Down()	
			
			
	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode
		self.RefreshBlock()

	def Show(self):
		self.RefreshMobile()
		self.RefreshBlock()
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
