import uiScriptLocale
import item

COSTUME_START_INDEX = item.COSTUME_SLOT_START

WINDOW_WIDTH = 135
WINDOW_HEIGTH = 140

window = {
	"name" : "CostumeWindow",

	"x" : SCREEN_WIDTH - 175 - 140 - 95,
	"y" : SCREEN_HEIGHT - 37 - 565 - 121,

	"style" : ("movable", "float",),

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30,

	"children" :
	(
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+30+15,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" :
			(
				# ## Title
				# {
					# "name" : "TitleBar",
					# "type" : "titlebar",
					# "style" : ("attach",),

					# "x" : 6,
					# "y" : 6,

					# "width" : 130,
					# "color" : "yellow",

					# "children" :
					# (
						# { "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"center" },
					# ),
				# },

				## Equipment Slot
				{
					"name" : "Costume_Base",
					"type" : "image",

					"x" : 25,
					"y" : 15,
					
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/costume_bg.jpg",					

					"children" :
					(

						{
							"name" : "CostumeSlot",
							"type" : "slot",

							"x" : 3,
							"y" : 3,

							"width" : 127,
							"height" : 145,

							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+2, "x":5, "y":145, "width":32, "height":32},
										{"index":item.EQUIPMENT_COSTUME_WEAPON, "x":15, "y":20, "width":32, "height":96},
									),
						},
					),
				},

			),
		},
	),
}
