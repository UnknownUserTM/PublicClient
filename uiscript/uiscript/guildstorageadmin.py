import uiScriptLocale

window = {
	"name" : "GuildStorageAdmin",

	"x" : SCREEN_WIDTH/2-520/2,
	"y" : SCREEN_HEIGHT/2-310/2,

	"style" : ("movable", "float",),

	"width" : 370+100+50,
	"height" : 310,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 370+100+50,
			"height" : 310,

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 370+100+50-15,

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":3, "text":'Gildenlager - Rechteverwaltung',"horizontal_align" : "center", "text_horizontal_align":"center",},
					),
				},
				
				################################
				## Adminpanel Tabelle START
				################################
				
				{
					"name": "GS_Adminpanel",
					
					"x" : 0,
					"y" : 40,
					
					"width" : 370,
					"height" : 300,
					
					"children": 
					(
						{
							"name" : "AP_label1",
							"type" : "text",
							
							"x" : 50,
							"y" : 0,
							
							"text" : "Name",
						},
						{
							"name" : "AP_label2",
							"type" : "text",
							
							"x" : 135,
							"y" : 0,
							
							"text" : "Einlagern",
						},
						{
							"name" : "AP_label3",
							"type" : "text",
							
							"x" : 189,
							"y" : 0,
							
							"text" : "Rausnehmen",
						},
						{
							"name" : "AP_label4",
							"type" : "text",
							
							"x" : 251,
							"y" : 0,
							
							"text" : "Einzahlen",
						},
						{
							"name" : "AP_label5",
							"type" : "text",
							
							"x" : 312,
							"y" : 0,
							
							"text" : "Abheben",
						},
					),
				},
				
				################################
				## Adminpanel Tabelle END
				################################
				
				################################
				## Menue START
				################################
				
				{
					"name" : "scrollbar",
					"type" : "scrollbar",

					"x" : 370+25-13,
					"y" : 40+17,

					"size" : 243,
				},
				{
					"name": "GS_Adminenue",
					
					"x" : 370+25,
					"y" : 40,
					
					"width" : 100,
					"height" : 300,
					
					"children": 
					(
						{
							"name" : "GS_AddMember", 
							"type" : "button",
							"text" : "Hinzufuegen",
							"x" : -2,
							"y" : 50,
							"horizontal_align" : "center",
							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
						},
						
						{
							"name" : "GS_MemberInputLineBG",
							"type" : "image",
							
							"x" : 0,
							"y" : 10,
			
							"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",
							
							"horizontal_align" : "center",
							
							"children" :
							(
								{
									"name" : "GS_MemberInputLine",
									"type" : "editline",
									
									"width" : 100,
									"height" : 14,
									
									"text"	: "Schnellsuche",
									
									"input_limit" : 15,
									
									"x" : 2,
									"y" : 2,
								},
							),
						},
					),
				},
				################################
				## Menue END
				################################
			),
		},
	),
}