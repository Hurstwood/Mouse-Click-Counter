import pyWinhook as pyHook
import pythoncom


def On_Mouse_Event(event):
	#print('MessageName: %s' % event.MessageName)
	#print('Message: %s' % event.Message)
	#print('Time: %s' % event.Time)
	#print('Window: %s' % event.Window)
	#print('WindowName: %s' % event.WindowName)
	#print('Position: (%d, %d)' % event.Position)
	#print('Wheel: %s' % event.Wheel)
	#print('Injected: %s' % event.Injected)
	#print('---')
	
	global clickTotal	
	clickTotal += 1
	print('Clicked {0} times'.format(clickTotal))

	# return True to pass the event to other handlers
	# return False to stop the event from propagating
	return True

	
def On_Keyboard_Event(event):
	# print('MessageName: %s' % event.MessageName)
	# print('Message: %s' % event.Message)
	# print('Time: %s' % event.Time)
	# print('Window: %s' % event.Window)
	# print('WindowName: %s' % event.WindowName)
	# print('Ascii: %s' %	event.Ascii, chr(event.Ascii))
	# print('Key: %s' %	event.Key)
	# print('KeyID: %s' %	event.KeyID)
	# print('ScanCode: %s' %	event.ScanCode)
	# print('Extended: %s' %	event.Extended)
	# print('Injected: %s' %	event.Injected)
	# print('Alt %s' %	event.Alt)
	# print('Transition %s' %	event.Transition)
	# print('---')

	
	ShiftButtonState = pyHook.GetKeyState(pyHook.HookConstants.vk_to_id["VK_LSHIFT"])	
	# Reset the count - Left shift + r
	if (ShiftButtonState == 128 and event.KeyID == 82):
		
		global clickTotal
		clickTotal = 0
		print('Reset')
	else: 
	
		ControlButtonState = pyHook.GetKeyState(pyHook.HookConstants.vk_to_id["VK_LCONTROL"])
		# Quit - Left control + c
		if (ControlButtonState == 128 and event.KeyID == 67):
			#print('Quit')
			exit()

	
	return True


# Global variables
clickTotal = 0

# Create the hook mananger
hookManager = pyHook.HookManager()

# Register two callbacks
# return True to pass the event to other handlers
# return False to stop the event from propagating

hookManager.MouseAllButtonsDown = On_Mouse_Event
hookManager.KeyDown = On_Keyboard_Event

# Hook into the mouse and keyboard events
hookManager.HookMouse()
hookManager.HookKeyboard()

	

if __name__ == '__main__':	
	pythoncom.PumpMessages()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	