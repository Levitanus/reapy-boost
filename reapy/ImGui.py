
import reapy
if reapy.is_inside_reaper():
    from reaper_python import *
# Generated for ReaImGui v0.5.9


@reapy.inside_reaper()
def AcceptDragDropPayload(ctx, type, payloadOutNeedBig = None, payloadOutNeedBig_sz = None, flagsInOptional = None):
  if not hasattr(AcceptDragDropPayload, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayload')
    AcceptDragDropPayload.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(type), rpr_packs(payloadOutNeedBig if payloadOutNeedBig != None else 0), c_int(payloadOutNeedBig_sz if payloadOutNeedBig_sz != None else 0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = AcceptDragDropPayload.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval, rpr_unpacks(args[2])

@reapy.inside_reaper()
def AcceptDragDropPayloadFiles(ctx, countOut = None, flagsInOptional = None):
  if not hasattr(AcceptDragDropPayloadFiles, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayloadFiles')
    AcceptDragDropPayloadFiles.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(countOut if countOut != None else 0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = AcceptDragDropPayloadFiles.func(args[0], byref(args[1]), byref(args[2]) if args[2] != None else None)
  return rval, int(args[1].value)

@reapy.inside_reaper()
def AcceptDragDropPayloadRGB(ctx, rgbOut = None, flagsInOptional = None):
  if not hasattr(AcceptDragDropPayloadRGB, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayloadRGB')
    AcceptDragDropPayloadRGB.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(rgbOut if rgbOut != None else 0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = AcceptDragDropPayloadRGB.func(args[0], byref(args[1]), byref(args[2]) if args[2] != None else None)
  return rval, int(args[1].value)

@reapy.inside_reaper()
def AcceptDragDropPayloadRGBA(ctx, rgbaOut = None, flagsInOptional = None):
  if not hasattr(AcceptDragDropPayloadRGBA, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayloadRGBA')
    AcceptDragDropPayloadRGBA.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(rgbaOut if rgbaOut != None else 0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = AcceptDragDropPayloadRGBA.func(args[0], byref(args[1]), byref(args[2]) if args[2] != None else None)
  return rval, int(args[1].value)

@reapy.inside_reaper()
def AlignTextToFramePadding(ctx):
  if not hasattr(AlignTextToFramePadding, 'func'):
    proc = rpr_getfp('ImGui_AlignTextToFramePadding')
    AlignTextToFramePadding.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  AlignTextToFramePadding.func(args[0])

@reapy.inside_reaper()
def ArrowButton(ctx, str_id, dir):
  if not hasattr(ArrowButton, 'func'):
    proc = rpr_getfp('ImGui_ArrowButton')
    ArrowButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_int(dir))
  rval = ArrowButton.func(args[0], args[1], args[2])
  return rval

@reapy.inside_reaper()
def AttachFont(ctx, font):
  if not hasattr(AttachFont, 'func'):
    proc = rpr_getfp('ImGui_AttachFont')
    AttachFont.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packp('Font*', font))
  AttachFont.func(args[0], args[1])

@reapy.inside_reaper()
def Begin(ctx, name, p_openInOutOptional = None, flagsInOptional = None):
  if not hasattr(Begin, 'func'):
    proc = rpr_getfp('ImGui_Begin')
    Begin.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(name), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = Begin.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value) if p_openInOutOptional != None else None

@reapy.inside_reaper()
def BeginChild(ctx, str_id, size_wInOptional = None, size_hInOptional = None, borderInOptional = None, flagsInOptional = None):
  if not hasattr(BeginChild, 'func'):
    proc = rpr_getfp('ImGui_BeginChild')
    BeginChild.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None, c_bool(borderInOptional) if borderInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginChild.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval

@reapy.inside_reaper()
def BeginChildFrame(ctx, str_id, size_w, size_h, flagsInOptional = None):
  if not hasattr(BeginChildFrame, 'func'):
    proc = rpr_getfp('ImGui_BeginChildFrame')
    BeginChildFrame.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_double(size_w), c_double(size_h), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginChildFrame.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval

@reapy.inside_reaper()
def BeginCombo(ctx, label, preview_value, flagsInOptional = None):
  if not hasattr(BeginCombo, 'func'):
    proc = rpr_getfp('ImGui_BeginCombo')
    BeginCombo.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packsc(preview_value), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginCombo.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

@reapy.inside_reaper()
def BeginDisabled(ctx, disabledInOptional = None):
  if not hasattr(BeginDisabled, 'func'):
    proc = rpr_getfp('ImGui_BeginDisabled')
    BeginDisabled.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(disabledInOptional) if disabledInOptional != None else None)
  BeginDisabled.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def BeginDragDropSource(ctx, flagsInOptional = None):
  if not hasattr(BeginDragDropSource, 'func'):
    proc = rpr_getfp('ImGui_BeginDragDropSource')
    BeginDragDropSource.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginDragDropSource.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

@reapy.inside_reaper()
def BeginDragDropTarget(ctx):
  if not hasattr(BeginDragDropTarget, 'func'):
    proc = rpr_getfp('ImGui_BeginDragDropTarget')
    BeginDragDropTarget.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = BeginDragDropTarget.func(args[0])
  return rval

@reapy.inside_reaper()
def BeginGroup(ctx):
  if not hasattr(BeginGroup, 'func'):
    proc = rpr_getfp('ImGui_BeginGroup')
    BeginGroup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  BeginGroup.func(args[0])

@reapy.inside_reaper()
def BeginListBox(ctx, label, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(BeginListBox, 'func'):
    proc = rpr_getfp('ImGui_BeginListBox')
    BeginListBox.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = BeginListBox.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval

@reapy.inside_reaper()
def BeginMenu(ctx, label, enabledInOptional = None):
  if not hasattr(BeginMenu, 'func'):
    proc = rpr_getfp('ImGui_BeginMenu')
    BeginMenu.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_bool(enabledInOptional) if enabledInOptional != None else None)
  rval = BeginMenu.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def BeginMenuBar(ctx):
  if not hasattr(BeginMenuBar, 'func'):
    proc = rpr_getfp('ImGui_BeginMenuBar')
    BeginMenuBar.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = BeginMenuBar.func(args[0])
  return rval

@reapy.inside_reaper()
def BeginPopup(ctx, str_id, flagsInOptional = None):
  if not hasattr(BeginPopup, 'func'):
    proc = rpr_getfp('ImGui_BeginPopup')
    BeginPopup.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginPopup.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def BeginPopupContextItem(ctx, str_idInOptional = None, popup_flagsInOptional = None):
  if not hasattr(BeginPopupContextItem, 'func'):
    proc = rpr_getfp('ImGui_BeginPopupContextItem')
    BeginPopupContextItem.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_idInOptional) if str_idInOptional != None else None, c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  rval = BeginPopupContextItem.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def BeginPopupContextWindow(ctx, str_idInOptional = None, popup_flagsInOptional = None):
  if not hasattr(BeginPopupContextWindow, 'func'):
    proc = rpr_getfp('ImGui_BeginPopupContextWindow')
    BeginPopupContextWindow.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_idInOptional) if str_idInOptional != None else None, c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  rval = BeginPopupContextWindow.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def BeginPopupModal(ctx, name, p_openInOutOptional = None, flagsInOptional = None):
  if not hasattr(BeginPopupModal, 'func'):
    proc = rpr_getfp('ImGui_BeginPopupModal')
    BeginPopupModal.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(name), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginPopupModal.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value) if p_openInOutOptional != None else None

@reapy.inside_reaper()
def BeginTabBar(ctx, str_id, flagsInOptional = None):
  if not hasattr(BeginTabBar, 'func'):
    proc = rpr_getfp('ImGui_BeginTabBar')
    BeginTabBar.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginTabBar.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def BeginTabItem(ctx, label, p_openInOutOptional = None, flagsInOptional = None):
  if not hasattr(BeginTabItem, 'func'):
    proc = rpr_getfp('ImGui_BeginTabItem')
    BeginTabItem.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = BeginTabItem.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value) if p_openInOutOptional != None else None

@reapy.inside_reaper()
def BeginTable(ctx, str_id, column, flagsInOptional = None, outer_size_wInOptional = None, outer_size_hInOptional = None, inner_widthInOptional = None):
  if not hasattr(BeginTable, 'func'):
    proc = rpr_getfp('ImGui_BeginTable')
    BeginTable.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_int(column), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(outer_size_wInOptional) if outer_size_wInOptional != None else None, c_double(outer_size_hInOptional) if outer_size_hInOptional != None else None, c_double(inner_widthInOptional) if inner_widthInOptional != None else None)
  rval = BeginTable.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)
  return rval

@reapy.inside_reaper()
def BeginTooltip(ctx):
  if not hasattr(BeginTooltip, 'func'):
    proc = rpr_getfp('ImGui_BeginTooltip')
    BeginTooltip.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  BeginTooltip.func(args[0])

@reapy.inside_reaper()
def Bullet(ctx):
  if not hasattr(Bullet, 'func'):
    proc = rpr_getfp('ImGui_Bullet')
    Bullet.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  Bullet.func(args[0])

@reapy.inside_reaper()
def BulletText(ctx, text):
  if not hasattr(BulletText, 'func'):
    proc = rpr_getfp('ImGui_BulletText')
    BulletText.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  BulletText.func(args[0], args[1])

@reapy.inside_reaper()
def Button(ctx, label, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(Button, 'func'):
    proc = rpr_getfp('ImGui_Button')
    Button.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = Button.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval

@reapy.inside_reaper()
def ButtonFlags_MouseButtonLeft():
  if not hasattr(ButtonFlags_MouseButtonLeft, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_MouseButtonLeft')
    ButtonFlags_MouseButtonLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ButtonFlags_MouseButtonLeft, 'cache'):
    ButtonFlags_MouseButtonLeft.cache = ButtonFlags_MouseButtonLeft.func()
  return ButtonFlags_MouseButtonLeft.cache

@reapy.inside_reaper()
def ButtonFlags_MouseButtonMiddle():
  if not hasattr(ButtonFlags_MouseButtonMiddle, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_MouseButtonMiddle')
    ButtonFlags_MouseButtonMiddle.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ButtonFlags_MouseButtonMiddle, 'cache'):
    ButtonFlags_MouseButtonMiddle.cache = ButtonFlags_MouseButtonMiddle.func()
  return ButtonFlags_MouseButtonMiddle.cache

@reapy.inside_reaper()
def ButtonFlags_MouseButtonRight():
  if not hasattr(ButtonFlags_MouseButtonRight, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_MouseButtonRight')
    ButtonFlags_MouseButtonRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ButtonFlags_MouseButtonRight, 'cache'):
    ButtonFlags_MouseButtonRight.cache = ButtonFlags_MouseButtonRight.func()
  return ButtonFlags_MouseButtonRight.cache

@reapy.inside_reaper()
def ButtonFlags_None():
  if not hasattr(ButtonFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_None')
    ButtonFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ButtonFlags_None, 'cache'):
    ButtonFlags_None.cache = ButtonFlags_None.func()
  return ButtonFlags_None.cache

@reapy.inside_reaper()
def CalcItemWidth(ctx):
  if not hasattr(CalcItemWidth, 'func'):
    proc = rpr_getfp('ImGui_CalcItemWidth')
    CalcItemWidth.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = CalcItemWidth.func(args[0])
  return rval

@reapy.inside_reaper()
def CalcTextSize(ctx, text, wOut = None, hOut = None, hide_text_after_double_hashInOptional = None, wrap_widthInOptional = None):
  if not hasattr(CalcTextSize, 'func'):
    proc = rpr_getfp('ImGui_CalcTextSize')
    CalcTextSize.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text), c_double(wOut if wOut != None else 0), c_double(hOut if hOut != None else 0), c_bool(hide_text_after_double_hashInOptional) if hide_text_after_double_hashInOptional != None else None, c_double(wrap_widthInOptional) if wrap_widthInOptional != None else None)
  CalcTextSize.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def CaptureKeyboardFromApp(ctx, want_capture_keyboard_valueInOptional = None):
  if not hasattr(CaptureKeyboardFromApp, 'func'):
    proc = rpr_getfp('ImGui_CaptureKeyboardFromApp')
    CaptureKeyboardFromApp.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(want_capture_keyboard_valueInOptional) if want_capture_keyboard_valueInOptional != None else None)
  CaptureKeyboardFromApp.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def Checkbox(ctx, label, vInOut):
  if not hasattr(Checkbox, 'func'):
    proc = rpr_getfp('ImGui_Checkbox')
    Checkbox.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_bool(vInOut))
  rval = Checkbox.func(args[0], args[1], byref(args[2]))
  return rval, int(args[2].value)

@reapy.inside_reaper()
def CheckboxFlags(ctx, label, flagsInOut, flags_value):
  if not hasattr(CheckboxFlags, 'func'):
    proc = rpr_getfp('ImGui_CheckboxFlags')
    CheckboxFlags.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(flagsInOut), c_int(flags_value))
  rval = CheckboxFlags.func(args[0], args[1], byref(args[2]), args[3])
  return rval, int(args[2].value)

@reapy.inside_reaper()
def CloseCurrentPopup(ctx):
  if not hasattr(CloseCurrentPopup, 'func'):
    proc = rpr_getfp('ImGui_CloseCurrentPopup')
    CloseCurrentPopup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  CloseCurrentPopup.func(args[0])

@reapy.inside_reaper()
def Col_Border():
  if not hasattr(Col_Border, 'func'):
    proc = rpr_getfp('ImGui_Col_Border')
    Col_Border.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_Border, 'cache'):
    Col_Border.cache = Col_Border.func()
  return Col_Border.cache

@reapy.inside_reaper()
def Col_BorderShadow():
  if not hasattr(Col_BorderShadow, 'func'):
    proc = rpr_getfp('ImGui_Col_BorderShadow')
    Col_BorderShadow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_BorderShadow, 'cache'):
    Col_BorderShadow.cache = Col_BorderShadow.func()
  return Col_BorderShadow.cache

@reapy.inside_reaper()
def Col_Button():
  if not hasattr(Col_Button, 'func'):
    proc = rpr_getfp('ImGui_Col_Button')
    Col_Button.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_Button, 'cache'):
    Col_Button.cache = Col_Button.func()
  return Col_Button.cache

@reapy.inside_reaper()
def Col_ButtonActive():
  if not hasattr(Col_ButtonActive, 'func'):
    proc = rpr_getfp('ImGui_Col_ButtonActive')
    Col_ButtonActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ButtonActive, 'cache'):
    Col_ButtonActive.cache = Col_ButtonActive.func()
  return Col_ButtonActive.cache

@reapy.inside_reaper()
def Col_ButtonHovered():
  if not hasattr(Col_ButtonHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_ButtonHovered')
    Col_ButtonHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ButtonHovered, 'cache'):
    Col_ButtonHovered.cache = Col_ButtonHovered.func()
  return Col_ButtonHovered.cache

@reapy.inside_reaper()
def Col_CheckMark():
  if not hasattr(Col_CheckMark, 'func'):
    proc = rpr_getfp('ImGui_Col_CheckMark')
    Col_CheckMark.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_CheckMark, 'cache'):
    Col_CheckMark.cache = Col_CheckMark.func()
  return Col_CheckMark.cache

@reapy.inside_reaper()
def Col_ChildBg():
  if not hasattr(Col_ChildBg, 'func'):
    proc = rpr_getfp('ImGui_Col_ChildBg')
    Col_ChildBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ChildBg, 'cache'):
    Col_ChildBg.cache = Col_ChildBg.func()
  return Col_ChildBg.cache

@reapy.inside_reaper()
def Col_DockingEmptyBg():
  if not hasattr(Col_DockingEmptyBg, 'func'):
    proc = rpr_getfp('ImGui_Col_DockingEmptyBg')
    Col_DockingEmptyBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_DockingEmptyBg, 'cache'):
    Col_DockingEmptyBg.cache = Col_DockingEmptyBg.func()
  return Col_DockingEmptyBg.cache

@reapy.inside_reaper()
def Col_DockingPreview():
  if not hasattr(Col_DockingPreview, 'func'):
    proc = rpr_getfp('ImGui_Col_DockingPreview')
    Col_DockingPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_DockingPreview, 'cache'):
    Col_DockingPreview.cache = Col_DockingPreview.func()
  return Col_DockingPreview.cache

@reapy.inside_reaper()
def Col_DragDropTarget():
  if not hasattr(Col_DragDropTarget, 'func'):
    proc = rpr_getfp('ImGui_Col_DragDropTarget')
    Col_DragDropTarget.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_DragDropTarget, 'cache'):
    Col_DragDropTarget.cache = Col_DragDropTarget.func()
  return Col_DragDropTarget.cache

@reapy.inside_reaper()
def Col_FrameBg():
  if not hasattr(Col_FrameBg, 'func'):
    proc = rpr_getfp('ImGui_Col_FrameBg')
    Col_FrameBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_FrameBg, 'cache'):
    Col_FrameBg.cache = Col_FrameBg.func()
  return Col_FrameBg.cache

@reapy.inside_reaper()
def Col_FrameBgActive():
  if not hasattr(Col_FrameBgActive, 'func'):
    proc = rpr_getfp('ImGui_Col_FrameBgActive')
    Col_FrameBgActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_FrameBgActive, 'cache'):
    Col_FrameBgActive.cache = Col_FrameBgActive.func()
  return Col_FrameBgActive.cache

@reapy.inside_reaper()
def Col_FrameBgHovered():
  if not hasattr(Col_FrameBgHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_FrameBgHovered')
    Col_FrameBgHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_FrameBgHovered, 'cache'):
    Col_FrameBgHovered.cache = Col_FrameBgHovered.func()
  return Col_FrameBgHovered.cache

@reapy.inside_reaper()
def Col_Header():
  if not hasattr(Col_Header, 'func'):
    proc = rpr_getfp('ImGui_Col_Header')
    Col_Header.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_Header, 'cache'):
    Col_Header.cache = Col_Header.func()
  return Col_Header.cache

@reapy.inside_reaper()
def Col_HeaderActive():
  if not hasattr(Col_HeaderActive, 'func'):
    proc = rpr_getfp('ImGui_Col_HeaderActive')
    Col_HeaderActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_HeaderActive, 'cache'):
    Col_HeaderActive.cache = Col_HeaderActive.func()
  return Col_HeaderActive.cache

@reapy.inside_reaper()
def Col_HeaderHovered():
  if not hasattr(Col_HeaderHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_HeaderHovered')
    Col_HeaderHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_HeaderHovered, 'cache'):
    Col_HeaderHovered.cache = Col_HeaderHovered.func()
  return Col_HeaderHovered.cache

@reapy.inside_reaper()
def Col_MenuBarBg():
  if not hasattr(Col_MenuBarBg, 'func'):
    proc = rpr_getfp('ImGui_Col_MenuBarBg')
    Col_MenuBarBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_MenuBarBg, 'cache'):
    Col_MenuBarBg.cache = Col_MenuBarBg.func()
  return Col_MenuBarBg.cache

@reapy.inside_reaper()
def Col_ModalWindowDimBg():
  if not hasattr(Col_ModalWindowDimBg, 'func'):
    proc = rpr_getfp('ImGui_Col_ModalWindowDimBg')
    Col_ModalWindowDimBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ModalWindowDimBg, 'cache'):
    Col_ModalWindowDimBg.cache = Col_ModalWindowDimBg.func()
  return Col_ModalWindowDimBg.cache

@reapy.inside_reaper()
def Col_NavHighlight():
  if not hasattr(Col_NavHighlight, 'func'):
    proc = rpr_getfp('ImGui_Col_NavHighlight')
    Col_NavHighlight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_NavHighlight, 'cache'):
    Col_NavHighlight.cache = Col_NavHighlight.func()
  return Col_NavHighlight.cache

@reapy.inside_reaper()
def Col_NavWindowingDimBg():
  if not hasattr(Col_NavWindowingDimBg, 'func'):
    proc = rpr_getfp('ImGui_Col_NavWindowingDimBg')
    Col_NavWindowingDimBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_NavWindowingDimBg, 'cache'):
    Col_NavWindowingDimBg.cache = Col_NavWindowingDimBg.func()
  return Col_NavWindowingDimBg.cache

@reapy.inside_reaper()
def Col_NavWindowingHighlight():
  if not hasattr(Col_NavWindowingHighlight, 'func'):
    proc = rpr_getfp('ImGui_Col_NavWindowingHighlight')
    Col_NavWindowingHighlight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_NavWindowingHighlight, 'cache'):
    Col_NavWindowingHighlight.cache = Col_NavWindowingHighlight.func()
  return Col_NavWindowingHighlight.cache

@reapy.inside_reaper()
def Col_PlotHistogram():
  if not hasattr(Col_PlotHistogram, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotHistogram')
    Col_PlotHistogram.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_PlotHistogram, 'cache'):
    Col_PlotHistogram.cache = Col_PlotHistogram.func()
  return Col_PlotHistogram.cache

@reapy.inside_reaper()
def Col_PlotHistogramHovered():
  if not hasattr(Col_PlotHistogramHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotHistogramHovered')
    Col_PlotHistogramHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_PlotHistogramHovered, 'cache'):
    Col_PlotHistogramHovered.cache = Col_PlotHistogramHovered.func()
  return Col_PlotHistogramHovered.cache

@reapy.inside_reaper()
def Col_PlotLines():
  if not hasattr(Col_PlotLines, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotLines')
    Col_PlotLines.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_PlotLines, 'cache'):
    Col_PlotLines.cache = Col_PlotLines.func()
  return Col_PlotLines.cache

@reapy.inside_reaper()
def Col_PlotLinesHovered():
  if not hasattr(Col_PlotLinesHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotLinesHovered')
    Col_PlotLinesHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_PlotLinesHovered, 'cache'):
    Col_PlotLinesHovered.cache = Col_PlotLinesHovered.func()
  return Col_PlotLinesHovered.cache

@reapy.inside_reaper()
def Col_PopupBg():
  if not hasattr(Col_PopupBg, 'func'):
    proc = rpr_getfp('ImGui_Col_PopupBg')
    Col_PopupBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_PopupBg, 'cache'):
    Col_PopupBg.cache = Col_PopupBg.func()
  return Col_PopupBg.cache

@reapy.inside_reaper()
def Col_ResizeGrip():
  if not hasattr(Col_ResizeGrip, 'func'):
    proc = rpr_getfp('ImGui_Col_ResizeGrip')
    Col_ResizeGrip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ResizeGrip, 'cache'):
    Col_ResizeGrip.cache = Col_ResizeGrip.func()
  return Col_ResizeGrip.cache

@reapy.inside_reaper()
def Col_ResizeGripActive():
  if not hasattr(Col_ResizeGripActive, 'func'):
    proc = rpr_getfp('ImGui_Col_ResizeGripActive')
    Col_ResizeGripActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ResizeGripActive, 'cache'):
    Col_ResizeGripActive.cache = Col_ResizeGripActive.func()
  return Col_ResizeGripActive.cache

@reapy.inside_reaper()
def Col_ResizeGripHovered():
  if not hasattr(Col_ResizeGripHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_ResizeGripHovered')
    Col_ResizeGripHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ResizeGripHovered, 'cache'):
    Col_ResizeGripHovered.cache = Col_ResizeGripHovered.func()
  return Col_ResizeGripHovered.cache

@reapy.inside_reaper()
def Col_ScrollbarBg():
  if not hasattr(Col_ScrollbarBg, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarBg')
    Col_ScrollbarBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ScrollbarBg, 'cache'):
    Col_ScrollbarBg.cache = Col_ScrollbarBg.func()
  return Col_ScrollbarBg.cache

@reapy.inside_reaper()
def Col_ScrollbarGrab():
  if not hasattr(Col_ScrollbarGrab, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarGrab')
    Col_ScrollbarGrab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ScrollbarGrab, 'cache'):
    Col_ScrollbarGrab.cache = Col_ScrollbarGrab.func()
  return Col_ScrollbarGrab.cache

@reapy.inside_reaper()
def Col_ScrollbarGrabActive():
  if not hasattr(Col_ScrollbarGrabActive, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarGrabActive')
    Col_ScrollbarGrabActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ScrollbarGrabActive, 'cache'):
    Col_ScrollbarGrabActive.cache = Col_ScrollbarGrabActive.func()
  return Col_ScrollbarGrabActive.cache

@reapy.inside_reaper()
def Col_ScrollbarGrabHovered():
  if not hasattr(Col_ScrollbarGrabHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarGrabHovered')
    Col_ScrollbarGrabHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_ScrollbarGrabHovered, 'cache'):
    Col_ScrollbarGrabHovered.cache = Col_ScrollbarGrabHovered.func()
  return Col_ScrollbarGrabHovered.cache

@reapy.inside_reaper()
def Col_Separator():
  if not hasattr(Col_Separator, 'func'):
    proc = rpr_getfp('ImGui_Col_Separator')
    Col_Separator.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_Separator, 'cache'):
    Col_Separator.cache = Col_Separator.func()
  return Col_Separator.cache

@reapy.inside_reaper()
def Col_SeparatorActive():
  if not hasattr(Col_SeparatorActive, 'func'):
    proc = rpr_getfp('ImGui_Col_SeparatorActive')
    Col_SeparatorActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_SeparatorActive, 'cache'):
    Col_SeparatorActive.cache = Col_SeparatorActive.func()
  return Col_SeparatorActive.cache

@reapy.inside_reaper()
def Col_SeparatorHovered():
  if not hasattr(Col_SeparatorHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_SeparatorHovered')
    Col_SeparatorHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_SeparatorHovered, 'cache'):
    Col_SeparatorHovered.cache = Col_SeparatorHovered.func()
  return Col_SeparatorHovered.cache

@reapy.inside_reaper()
def Col_SliderGrab():
  if not hasattr(Col_SliderGrab, 'func'):
    proc = rpr_getfp('ImGui_Col_SliderGrab')
    Col_SliderGrab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_SliderGrab, 'cache'):
    Col_SliderGrab.cache = Col_SliderGrab.func()
  return Col_SliderGrab.cache

@reapy.inside_reaper()
def Col_SliderGrabActive():
  if not hasattr(Col_SliderGrabActive, 'func'):
    proc = rpr_getfp('ImGui_Col_SliderGrabActive')
    Col_SliderGrabActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_SliderGrabActive, 'cache'):
    Col_SliderGrabActive.cache = Col_SliderGrabActive.func()
  return Col_SliderGrabActive.cache

@reapy.inside_reaper()
def Col_Tab():
  if not hasattr(Col_Tab, 'func'):
    proc = rpr_getfp('ImGui_Col_Tab')
    Col_Tab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_Tab, 'cache'):
    Col_Tab.cache = Col_Tab.func()
  return Col_Tab.cache

@reapy.inside_reaper()
def Col_TabActive():
  if not hasattr(Col_TabActive, 'func'):
    proc = rpr_getfp('ImGui_Col_TabActive')
    Col_TabActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TabActive, 'cache'):
    Col_TabActive.cache = Col_TabActive.func()
  return Col_TabActive.cache

@reapy.inside_reaper()
def Col_TabHovered():
  if not hasattr(Col_TabHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_TabHovered')
    Col_TabHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TabHovered, 'cache'):
    Col_TabHovered.cache = Col_TabHovered.func()
  return Col_TabHovered.cache

@reapy.inside_reaper()
def Col_TabUnfocused():
  if not hasattr(Col_TabUnfocused, 'func'):
    proc = rpr_getfp('ImGui_Col_TabUnfocused')
    Col_TabUnfocused.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TabUnfocused, 'cache'):
    Col_TabUnfocused.cache = Col_TabUnfocused.func()
  return Col_TabUnfocused.cache

@reapy.inside_reaper()
def Col_TabUnfocusedActive():
  if not hasattr(Col_TabUnfocusedActive, 'func'):
    proc = rpr_getfp('ImGui_Col_TabUnfocusedActive')
    Col_TabUnfocusedActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TabUnfocusedActive, 'cache'):
    Col_TabUnfocusedActive.cache = Col_TabUnfocusedActive.func()
  return Col_TabUnfocusedActive.cache

@reapy.inside_reaper()
def Col_TableBorderLight():
  if not hasattr(Col_TableBorderLight, 'func'):
    proc = rpr_getfp('ImGui_Col_TableBorderLight')
    Col_TableBorderLight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TableBorderLight, 'cache'):
    Col_TableBorderLight.cache = Col_TableBorderLight.func()
  return Col_TableBorderLight.cache

@reapy.inside_reaper()
def Col_TableBorderStrong():
  if not hasattr(Col_TableBorderStrong, 'func'):
    proc = rpr_getfp('ImGui_Col_TableBorderStrong')
    Col_TableBorderStrong.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TableBorderStrong, 'cache'):
    Col_TableBorderStrong.cache = Col_TableBorderStrong.func()
  return Col_TableBorderStrong.cache

@reapy.inside_reaper()
def Col_TableHeaderBg():
  if not hasattr(Col_TableHeaderBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TableHeaderBg')
    Col_TableHeaderBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TableHeaderBg, 'cache'):
    Col_TableHeaderBg.cache = Col_TableHeaderBg.func()
  return Col_TableHeaderBg.cache

@reapy.inside_reaper()
def Col_TableRowBg():
  if not hasattr(Col_TableRowBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TableRowBg')
    Col_TableRowBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TableRowBg, 'cache'):
    Col_TableRowBg.cache = Col_TableRowBg.func()
  return Col_TableRowBg.cache

@reapy.inside_reaper()
def Col_TableRowBgAlt():
  if not hasattr(Col_TableRowBgAlt, 'func'):
    proc = rpr_getfp('ImGui_Col_TableRowBgAlt')
    Col_TableRowBgAlt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TableRowBgAlt, 'cache'):
    Col_TableRowBgAlt.cache = Col_TableRowBgAlt.func()
  return Col_TableRowBgAlt.cache

@reapy.inside_reaper()
def Col_Text():
  if not hasattr(Col_Text, 'func'):
    proc = rpr_getfp('ImGui_Col_Text')
    Col_Text.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_Text, 'cache'):
    Col_Text.cache = Col_Text.func()
  return Col_Text.cache

@reapy.inside_reaper()
def Col_TextDisabled():
  if not hasattr(Col_TextDisabled, 'func'):
    proc = rpr_getfp('ImGui_Col_TextDisabled')
    Col_TextDisabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TextDisabled, 'cache'):
    Col_TextDisabled.cache = Col_TextDisabled.func()
  return Col_TextDisabled.cache

@reapy.inside_reaper()
def Col_TextSelectedBg():
  if not hasattr(Col_TextSelectedBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TextSelectedBg')
    Col_TextSelectedBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TextSelectedBg, 'cache'):
    Col_TextSelectedBg.cache = Col_TextSelectedBg.func()
  return Col_TextSelectedBg.cache

@reapy.inside_reaper()
def Col_TitleBg():
  if not hasattr(Col_TitleBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TitleBg')
    Col_TitleBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TitleBg, 'cache'):
    Col_TitleBg.cache = Col_TitleBg.func()
  return Col_TitleBg.cache

@reapy.inside_reaper()
def Col_TitleBgActive():
  if not hasattr(Col_TitleBgActive, 'func'):
    proc = rpr_getfp('ImGui_Col_TitleBgActive')
    Col_TitleBgActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TitleBgActive, 'cache'):
    Col_TitleBgActive.cache = Col_TitleBgActive.func()
  return Col_TitleBgActive.cache

@reapy.inside_reaper()
def Col_TitleBgCollapsed():
  if not hasattr(Col_TitleBgCollapsed, 'func'):
    proc = rpr_getfp('ImGui_Col_TitleBgCollapsed')
    Col_TitleBgCollapsed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_TitleBgCollapsed, 'cache'):
    Col_TitleBgCollapsed.cache = Col_TitleBgCollapsed.func()
  return Col_TitleBgCollapsed.cache

@reapy.inside_reaper()
def Col_WindowBg():
  if not hasattr(Col_WindowBg, 'func'):
    proc = rpr_getfp('ImGui_Col_WindowBg')
    Col_WindowBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Col_WindowBg, 'cache'):
    Col_WindowBg.cache = Col_WindowBg.func()
  return Col_WindowBg.cache

@reapy.inside_reaper()
def CollapsingHeader(ctx, label, p_visibleInOut, flagsInOptional = None):
  if not hasattr(CollapsingHeader, 'func'):
    proc = rpr_getfp('ImGui_CollapsingHeader')
    CollapsingHeader.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_bool(p_visibleInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = CollapsingHeader.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ColorButton(ctx, desc_id, col_rgba, flagsInOptional = None, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(ColorButton, 'func'):
    proc = rpr_getfp('ImGui_ColorButton')
    ColorButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(desc_id), c_int(col_rgba), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = ColorButton.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval

@reapy.inside_reaper()
def ColorConvertHSVtoRGB(h, s, v, alphaInOptional = None, rOut = None, gOut = None, bOut = None):
  if not hasattr(ColorConvertHSVtoRGB, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertHSVtoRGB')
    ColorConvertHSVtoRGB.func = CFUNCTYPE(c_int, c_double, c_double, c_double, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (c_double(h), c_double(s), c_double(v), c_double(alphaInOptional) if alphaInOptional != None else None, c_double(rOut if rOut != None else 0), c_double(gOut if gOut != None else 0), c_double(bOut if bOut != None else 0))
  rval = ColorConvertHSVtoRGB.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]), byref(args[5]), byref(args[6]))
  return rval, float(args[4].value), float(args[5].value), float(args[6].value)

@reapy.inside_reaper()
def ColorConvertNative(rgb):
  if not hasattr(ColorConvertNative, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertNative')
    ColorConvertNative.func = CFUNCTYPE(c_int, c_int)(proc)
  args = (c_int(rgb),)
  rval = ColorConvertNative.func(args[0])
  return rval

@reapy.inside_reaper()
def ColorConvertRGBtoHSV(r, g, b, alphaInOptional = None, hOut = None, sOut = None, vOut = None):
  if not hasattr(ColorConvertRGBtoHSV, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertRGBtoHSV')
    ColorConvertRGBtoHSV.func = CFUNCTYPE(c_int, c_double, c_double, c_double, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (c_double(r), c_double(g), c_double(b), c_double(alphaInOptional) if alphaInOptional != None else None, c_double(hOut if hOut != None else 0), c_double(sOut if sOut != None else 0), c_double(vOut if vOut != None else 0))
  rval = ColorConvertRGBtoHSV.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]), byref(args[5]), byref(args[6]))
  return rval, float(args[4].value), float(args[5].value), float(args[6].value)

@reapy.inside_reaper()
def ColorEdit3(ctx, label, col_rgbInOut, flagsInOptional = None):
  if not hasattr(ColorEdit3, 'func'):
    proc = rpr_getfp('ImGui_ColorEdit3')
    ColorEdit3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(col_rgbInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ColorEdit3.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ColorEdit4(ctx, label, col_rgbaInOut, flagsInOptional = None):
  if not hasattr(ColorEdit4, 'func'):
    proc = rpr_getfp('ImGui_ColorEdit4')
    ColorEdit4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(col_rgbaInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ColorEdit4.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ColorEditFlags_AlphaBar():
  if not hasattr(ColorEditFlags_AlphaBar, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_AlphaBar')
    ColorEditFlags_AlphaBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_AlphaBar, 'cache'):
    ColorEditFlags_AlphaBar.cache = ColorEditFlags_AlphaBar.func()
  return ColorEditFlags_AlphaBar.cache

@reapy.inside_reaper()
def ColorEditFlags_AlphaPreview():
  if not hasattr(ColorEditFlags_AlphaPreview, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_AlphaPreview')
    ColorEditFlags_AlphaPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_AlphaPreview, 'cache'):
    ColorEditFlags_AlphaPreview.cache = ColorEditFlags_AlphaPreview.func()
  return ColorEditFlags_AlphaPreview.cache

@reapy.inside_reaper()
def ColorEditFlags_AlphaPreviewHalf():
  if not hasattr(ColorEditFlags_AlphaPreviewHalf, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_AlphaPreviewHalf')
    ColorEditFlags_AlphaPreviewHalf.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_AlphaPreviewHalf, 'cache'):
    ColorEditFlags_AlphaPreviewHalf.cache = ColorEditFlags_AlphaPreviewHalf.func()
  return ColorEditFlags_AlphaPreviewHalf.cache

@reapy.inside_reaper()
def ColorEditFlags_DisplayHSV():
  if not hasattr(ColorEditFlags_DisplayHSV, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_DisplayHSV')
    ColorEditFlags_DisplayHSV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_DisplayHSV, 'cache'):
    ColorEditFlags_DisplayHSV.cache = ColorEditFlags_DisplayHSV.func()
  return ColorEditFlags_DisplayHSV.cache

@reapy.inside_reaper()
def ColorEditFlags_DisplayHex():
  if not hasattr(ColorEditFlags_DisplayHex, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_DisplayHex')
    ColorEditFlags_DisplayHex.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_DisplayHex, 'cache'):
    ColorEditFlags_DisplayHex.cache = ColorEditFlags_DisplayHex.func()
  return ColorEditFlags_DisplayHex.cache

@reapy.inside_reaper()
def ColorEditFlags_DisplayRGB():
  if not hasattr(ColorEditFlags_DisplayRGB, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_DisplayRGB')
    ColorEditFlags_DisplayRGB.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_DisplayRGB, 'cache'):
    ColorEditFlags_DisplayRGB.cache = ColorEditFlags_DisplayRGB.func()
  return ColorEditFlags_DisplayRGB.cache

@reapy.inside_reaper()
def ColorEditFlags_Float():
  if not hasattr(ColorEditFlags_Float, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_Float')
    ColorEditFlags_Float.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_Float, 'cache'):
    ColorEditFlags_Float.cache = ColorEditFlags_Float.func()
  return ColorEditFlags_Float.cache

@reapy.inside_reaper()
def ColorEditFlags_InputHSV():
  if not hasattr(ColorEditFlags_InputHSV, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_InputHSV')
    ColorEditFlags_InputHSV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_InputHSV, 'cache'):
    ColorEditFlags_InputHSV.cache = ColorEditFlags_InputHSV.func()
  return ColorEditFlags_InputHSV.cache

@reapy.inside_reaper()
def ColorEditFlags_InputRGB():
  if not hasattr(ColorEditFlags_InputRGB, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_InputRGB')
    ColorEditFlags_InputRGB.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_InputRGB, 'cache'):
    ColorEditFlags_InputRGB.cache = ColorEditFlags_InputRGB.func()
  return ColorEditFlags_InputRGB.cache

@reapy.inside_reaper()
def ColorEditFlags_NoAlpha():
  if not hasattr(ColorEditFlags_NoAlpha, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoAlpha')
    ColorEditFlags_NoAlpha.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoAlpha, 'cache'):
    ColorEditFlags_NoAlpha.cache = ColorEditFlags_NoAlpha.func()
  return ColorEditFlags_NoAlpha.cache

@reapy.inside_reaper()
def ColorEditFlags_NoBorder():
  if not hasattr(ColorEditFlags_NoBorder, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoBorder')
    ColorEditFlags_NoBorder.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoBorder, 'cache'):
    ColorEditFlags_NoBorder.cache = ColorEditFlags_NoBorder.func()
  return ColorEditFlags_NoBorder.cache

@reapy.inside_reaper()
def ColorEditFlags_NoDragDrop():
  if not hasattr(ColorEditFlags_NoDragDrop, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoDragDrop')
    ColorEditFlags_NoDragDrop.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoDragDrop, 'cache'):
    ColorEditFlags_NoDragDrop.cache = ColorEditFlags_NoDragDrop.func()
  return ColorEditFlags_NoDragDrop.cache

@reapy.inside_reaper()
def ColorEditFlags_NoInputs():
  if not hasattr(ColorEditFlags_NoInputs, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoInputs')
    ColorEditFlags_NoInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoInputs, 'cache'):
    ColorEditFlags_NoInputs.cache = ColorEditFlags_NoInputs.func()
  return ColorEditFlags_NoInputs.cache

@reapy.inside_reaper()
def ColorEditFlags_NoLabel():
  if not hasattr(ColorEditFlags_NoLabel, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoLabel')
    ColorEditFlags_NoLabel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoLabel, 'cache'):
    ColorEditFlags_NoLabel.cache = ColorEditFlags_NoLabel.func()
  return ColorEditFlags_NoLabel.cache

@reapy.inside_reaper()
def ColorEditFlags_NoOptions():
  if not hasattr(ColorEditFlags_NoOptions, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoOptions')
    ColorEditFlags_NoOptions.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoOptions, 'cache'):
    ColorEditFlags_NoOptions.cache = ColorEditFlags_NoOptions.func()
  return ColorEditFlags_NoOptions.cache

@reapy.inside_reaper()
def ColorEditFlags_NoPicker():
  if not hasattr(ColorEditFlags_NoPicker, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoPicker')
    ColorEditFlags_NoPicker.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoPicker, 'cache'):
    ColorEditFlags_NoPicker.cache = ColorEditFlags_NoPicker.func()
  return ColorEditFlags_NoPicker.cache

@reapy.inside_reaper()
def ColorEditFlags_NoSidePreview():
  if not hasattr(ColorEditFlags_NoSidePreview, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoSidePreview')
    ColorEditFlags_NoSidePreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoSidePreview, 'cache'):
    ColorEditFlags_NoSidePreview.cache = ColorEditFlags_NoSidePreview.func()
  return ColorEditFlags_NoSidePreview.cache

@reapy.inside_reaper()
def ColorEditFlags_NoSmallPreview():
  if not hasattr(ColorEditFlags_NoSmallPreview, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoSmallPreview')
    ColorEditFlags_NoSmallPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoSmallPreview, 'cache'):
    ColorEditFlags_NoSmallPreview.cache = ColorEditFlags_NoSmallPreview.func()
  return ColorEditFlags_NoSmallPreview.cache

@reapy.inside_reaper()
def ColorEditFlags_NoTooltip():
  if not hasattr(ColorEditFlags_NoTooltip, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoTooltip')
    ColorEditFlags_NoTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_NoTooltip, 'cache'):
    ColorEditFlags_NoTooltip.cache = ColorEditFlags_NoTooltip.func()
  return ColorEditFlags_NoTooltip.cache

@reapy.inside_reaper()
def ColorEditFlags_None():
  if not hasattr(ColorEditFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_None')
    ColorEditFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_None, 'cache'):
    ColorEditFlags_None.cache = ColorEditFlags_None.func()
  return ColorEditFlags_None.cache

@reapy.inside_reaper()
def ColorEditFlags_PickerHueBar():
  if not hasattr(ColorEditFlags_PickerHueBar, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_PickerHueBar')
    ColorEditFlags_PickerHueBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_PickerHueBar, 'cache'):
    ColorEditFlags_PickerHueBar.cache = ColorEditFlags_PickerHueBar.func()
  return ColorEditFlags_PickerHueBar.cache

@reapy.inside_reaper()
def ColorEditFlags_PickerHueWheel():
  if not hasattr(ColorEditFlags_PickerHueWheel, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_PickerHueWheel')
    ColorEditFlags_PickerHueWheel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_PickerHueWheel, 'cache'):
    ColorEditFlags_PickerHueWheel.cache = ColorEditFlags_PickerHueWheel.func()
  return ColorEditFlags_PickerHueWheel.cache

@reapy.inside_reaper()
def ColorEditFlags_Uint8():
  if not hasattr(ColorEditFlags_Uint8, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_Uint8')
    ColorEditFlags_Uint8.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ColorEditFlags_Uint8, 'cache'):
    ColorEditFlags_Uint8.cache = ColorEditFlags_Uint8.func()
  return ColorEditFlags_Uint8.cache

@reapy.inside_reaper()
def ColorPicker3(ctx, label, col_rgbInOut, flagsInOptional = None):
  if not hasattr(ColorPicker3, 'func'):
    proc = rpr_getfp('ImGui_ColorPicker3')
    ColorPicker3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(col_rgbInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ColorPicker3.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ColorPicker4(ctx, label, col_rgbaInOut, flagsInOptional = None, ref_colInOptional = None):
  if not hasattr(ColorPicker4, 'func'):
    proc = rpr_getfp('ImGui_ColorPicker4')
    ColorPicker4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(col_rgbaInOut), c_int(flagsInOptional) if flagsInOptional != None else None, c_int(ref_colInOptional) if ref_colInOptional != None else None)
  rval = ColorPicker4.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def Combo(ctx, label, current_itemInOut, items, popup_max_height_in_itemsInOptional = None):
  if not hasattr(Combo, 'func'):
    proc = rpr_getfp('ImGui_Combo')
    Combo.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(current_itemInOut), rpr_packs(items), c_int(popup_max_height_in_itemsInOptional) if popup_max_height_in_itemsInOptional != None else None)
  rval = Combo.func(args[0], args[1], byref(args[2]), args[3], byref(args[4]) if args[4] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ComboFlags_HeightLarge():
  if not hasattr(ComboFlags_HeightLarge, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightLarge')
    ComboFlags_HeightLarge.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_HeightLarge, 'cache'):
    ComboFlags_HeightLarge.cache = ComboFlags_HeightLarge.func()
  return ComboFlags_HeightLarge.cache

@reapy.inside_reaper()
def ComboFlags_HeightLargest():
  if not hasattr(ComboFlags_HeightLargest, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightLargest')
    ComboFlags_HeightLargest.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_HeightLargest, 'cache'):
    ComboFlags_HeightLargest.cache = ComboFlags_HeightLargest.func()
  return ComboFlags_HeightLargest.cache

@reapy.inside_reaper()
def ComboFlags_HeightRegular():
  if not hasattr(ComboFlags_HeightRegular, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightRegular')
    ComboFlags_HeightRegular.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_HeightRegular, 'cache'):
    ComboFlags_HeightRegular.cache = ComboFlags_HeightRegular.func()
  return ComboFlags_HeightRegular.cache

@reapy.inside_reaper()
def ComboFlags_HeightSmall():
  if not hasattr(ComboFlags_HeightSmall, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightSmall')
    ComboFlags_HeightSmall.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_HeightSmall, 'cache'):
    ComboFlags_HeightSmall.cache = ComboFlags_HeightSmall.func()
  return ComboFlags_HeightSmall.cache

@reapy.inside_reaper()
def ComboFlags_NoArrowButton():
  if not hasattr(ComboFlags_NoArrowButton, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_NoArrowButton')
    ComboFlags_NoArrowButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_NoArrowButton, 'cache'):
    ComboFlags_NoArrowButton.cache = ComboFlags_NoArrowButton.func()
  return ComboFlags_NoArrowButton.cache

@reapy.inside_reaper()
def ComboFlags_NoPreview():
  if not hasattr(ComboFlags_NoPreview, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_NoPreview')
    ComboFlags_NoPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_NoPreview, 'cache'):
    ComboFlags_NoPreview.cache = ComboFlags_NoPreview.func()
  return ComboFlags_NoPreview.cache

@reapy.inside_reaper()
def ComboFlags_None():
  if not hasattr(ComboFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_None')
    ComboFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_None, 'cache'):
    ComboFlags_None.cache = ComboFlags_None.func()
  return ComboFlags_None.cache

@reapy.inside_reaper()
def ComboFlags_PopupAlignLeft():
  if not hasattr(ComboFlags_PopupAlignLeft, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_PopupAlignLeft')
    ComboFlags_PopupAlignLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ComboFlags_PopupAlignLeft, 'cache'):
    ComboFlags_PopupAlignLeft.cache = ComboFlags_PopupAlignLeft.func()
  return ComboFlags_PopupAlignLeft.cache

@reapy.inside_reaper()
def Cond_Always():
  if not hasattr(Cond_Always, 'func'):
    proc = rpr_getfp('ImGui_Cond_Always')
    Cond_Always.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Cond_Always, 'cache'):
    Cond_Always.cache = Cond_Always.func()
  return Cond_Always.cache

@reapy.inside_reaper()
def Cond_Appearing():
  if not hasattr(Cond_Appearing, 'func'):
    proc = rpr_getfp('ImGui_Cond_Appearing')
    Cond_Appearing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Cond_Appearing, 'cache'):
    Cond_Appearing.cache = Cond_Appearing.func()
  return Cond_Appearing.cache

@reapy.inside_reaper()
def Cond_FirstUseEver():
  if not hasattr(Cond_FirstUseEver, 'func'):
    proc = rpr_getfp('ImGui_Cond_FirstUseEver')
    Cond_FirstUseEver.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Cond_FirstUseEver, 'cache'):
    Cond_FirstUseEver.cache = Cond_FirstUseEver.func()
  return Cond_FirstUseEver.cache

@reapy.inside_reaper()
def Cond_Once():
  if not hasattr(Cond_Once, 'func'):
    proc = rpr_getfp('ImGui_Cond_Once')
    Cond_Once.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Cond_Once, 'cache'):
    Cond_Once.cache = Cond_Once.func()
  return Cond_Once.cache

@reapy.inside_reaper()
def ConfigFlags_DockingEnable():
  if not hasattr(ConfigFlags_DockingEnable, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_DockingEnable')
    ConfigFlags_DockingEnable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_DockingEnable, 'cache'):
    ConfigFlags_DockingEnable.cache = ConfigFlags_DockingEnable.func()
  return ConfigFlags_DockingEnable.cache

@reapy.inside_reaper()
def ConfigFlags_NavEnableKeyboard():
  if not hasattr(ConfigFlags_NavEnableKeyboard, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NavEnableKeyboard')
    ConfigFlags_NavEnableKeyboard.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_NavEnableKeyboard, 'cache'):
    ConfigFlags_NavEnableKeyboard.cache = ConfigFlags_NavEnableKeyboard.func()
  return ConfigFlags_NavEnableKeyboard.cache

@reapy.inside_reaper()
def ConfigFlags_NavEnableSetMousePos():
  if not hasattr(ConfigFlags_NavEnableSetMousePos, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NavEnableSetMousePos')
    ConfigFlags_NavEnableSetMousePos.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_NavEnableSetMousePos, 'cache'):
    ConfigFlags_NavEnableSetMousePos.cache = ConfigFlags_NavEnableSetMousePos.func()
  return ConfigFlags_NavEnableSetMousePos.cache

@reapy.inside_reaper()
def ConfigFlags_NoMouse():
  if not hasattr(ConfigFlags_NoMouse, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NoMouse')
    ConfigFlags_NoMouse.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_NoMouse, 'cache'):
    ConfigFlags_NoMouse.cache = ConfigFlags_NoMouse.func()
  return ConfigFlags_NoMouse.cache

@reapy.inside_reaper()
def ConfigFlags_NoMouseCursorChange():
  if not hasattr(ConfigFlags_NoMouseCursorChange, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NoMouseCursorChange')
    ConfigFlags_NoMouseCursorChange.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_NoMouseCursorChange, 'cache'):
    ConfigFlags_NoMouseCursorChange.cache = ConfigFlags_NoMouseCursorChange.func()
  return ConfigFlags_NoMouseCursorChange.cache

@reapy.inside_reaper()
def ConfigFlags_NoSavedSettings():
  if not hasattr(ConfigFlags_NoSavedSettings, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NoSavedSettings')
    ConfigFlags_NoSavedSettings.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_NoSavedSettings, 'cache'):
    ConfigFlags_NoSavedSettings.cache = ConfigFlags_NoSavedSettings.func()
  return ConfigFlags_NoSavedSettings.cache

@reapy.inside_reaper()
def ConfigFlags_None():
  if not hasattr(ConfigFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_None')
    ConfigFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ConfigFlags_None, 'cache'):
    ConfigFlags_None.cache = ConfigFlags_None.func()
  return ConfigFlags_None.cache

@reapy.inside_reaper()
def CreateContext(label, config_flagsInOptional = None):
  if not hasattr(CreateContext, 'func'):
    proc = rpr_getfp('ImGui_CreateContext')
    CreateContext.func = CFUNCTYPE(c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packsc(label), c_int(config_flagsInOptional) if config_flagsInOptional != None else None)
  rval = CreateContext.func(args[0], byref(args[1]) if args[1] != None else None)
  return rpr_unpackp('Context*', rval)

@reapy.inside_reaper()
def CreateFont(family_or_file, size, flagsInOptional = None):
  if not hasattr(CreateFont, 'func'):
    proc = rpr_getfp('ImGui_CreateFont')
    CreateFont.func = CFUNCTYPE(c_void_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packsc(family_or_file), c_int(size), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = CreateFont.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rpr_unpackp('Font*', rval)

@reapy.inside_reaper()
def CreateListClipper(ctx):
  if not hasattr(CreateListClipper, 'func'):
    proc = rpr_getfp('ImGui_CreateListClipper')
    CreateListClipper.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = CreateListClipper.func(args[0])
  return rpr_unpackp('ListClipper*', rval)

@reapy.inside_reaper()
def CreateTextFilter(default_filterInOptional = None):
  if not hasattr(CreateTextFilter, 'func'):
    proc = rpr_getfp('ImGui_CreateTextFilter')
    CreateTextFilter.func = CFUNCTYPE(c_void_p, c_char_p)(proc)
  args = (rpr_packsc(default_filterInOptional) if default_filterInOptional != None else None,)
  rval = CreateTextFilter.func(args[0])
  return rpr_unpackp('TextFilter*', rval)

@reapy.inside_reaper()
def DestroyContext(ctx):
  if not hasattr(DestroyContext, 'func'):
    proc = rpr_getfp('ImGui_DestroyContext')
    DestroyContext.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  DestroyContext.func(args[0])

@reapy.inside_reaper()
def DetachFont(ctx, font):
  if not hasattr(DetachFont, 'func'):
    proc = rpr_getfp('ImGui_DetachFont')
    DetachFont.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packp('Font*', font))
  DetachFont.func(args[0], args[1])

@reapy.inside_reaper()
def Dir_Down():
  if not hasattr(Dir_Down, 'func'):
    proc = rpr_getfp('ImGui_Dir_Down')
    Dir_Down.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Dir_Down, 'cache'):
    Dir_Down.cache = Dir_Down.func()
  return Dir_Down.cache

@reapy.inside_reaper()
def Dir_Left():
  if not hasattr(Dir_Left, 'func'):
    proc = rpr_getfp('ImGui_Dir_Left')
    Dir_Left.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Dir_Left, 'cache'):
    Dir_Left.cache = Dir_Left.func()
  return Dir_Left.cache

@reapy.inside_reaper()
def Dir_None():
  if not hasattr(Dir_None, 'func'):
    proc = rpr_getfp('ImGui_Dir_None')
    Dir_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Dir_None, 'cache'):
    Dir_None.cache = Dir_None.func()
  return Dir_None.cache

@reapy.inside_reaper()
def Dir_Right():
  if not hasattr(Dir_Right, 'func'):
    proc = rpr_getfp('ImGui_Dir_Right')
    Dir_Right.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Dir_Right, 'cache'):
    Dir_Right.cache = Dir_Right.func()
  return Dir_Right.cache

@reapy.inside_reaper()
def Dir_Up():
  if not hasattr(Dir_Up, 'func'):
    proc = rpr_getfp('ImGui_Dir_Up')
    Dir_Up.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(Dir_Up, 'cache'):
    Dir_Up.cache = Dir_Up.func()
  return Dir_Up.cache

@reapy.inside_reaper()
def DragDouble(ctx, label, vInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragDouble, 'func'):
    proc = rpr_getfp('ImGui_DragDouble')
    DragDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(vInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragDouble.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, args[6], byref(args[7]) if args[7] != None else None)
  return rval, float(args[2].value)

@reapy.inside_reaper()
def DragDouble2(ctx, label, v1InOut, v2InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragDouble2, 'func'):
    proc = rpr_getfp('ImGui_DragDouble2')
    DragDouble2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragDouble2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], byref(args[8]) if args[8] != None else None)
  return rval, float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def DragDouble3(ctx, label, v1InOut, v2InOut, v3InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragDouble3, 'func'):
    proc = rpr_getfp('ImGui_DragDouble3')
    DragDouble3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragDouble3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, args[8], byref(args[9]) if args[9] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value)

@reapy.inside_reaper()
def DragDouble4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragDouble4, 'func'):
    proc = rpr_getfp('ImGui_DragDouble4')
    DragDouble4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v4InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragDouble4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None, args[9], byref(args[10]) if args[10] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value), float(args[5].value)

@reapy.inside_reaper()
def DragDoubleN(ctx, label, values, speedInOptional = None, minInOptional = None, maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragDoubleN, 'func'):
    proc = rpr_getfp('ImGui_DragDoubleN')
    DragDoubleN.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_double(speedInOptional) if speedInOptional != None else None, c_double(minInOptional) if minInOptional != None else None, c_double(maxInOptional) if maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragDoubleN.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, args[6], byref(args[7]) if args[7] != None else None)
  return rval

@reapy.inside_reaper()
def DragDropFlags_AcceptBeforeDelivery():
  if not hasattr(DragDropFlags_AcceptBeforeDelivery, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptBeforeDelivery')
    DragDropFlags_AcceptBeforeDelivery.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_AcceptBeforeDelivery, 'cache'):
    DragDropFlags_AcceptBeforeDelivery.cache = DragDropFlags_AcceptBeforeDelivery.func()
  return DragDropFlags_AcceptBeforeDelivery.cache

@reapy.inside_reaper()
def DragDropFlags_AcceptNoDrawDefaultRect():
  if not hasattr(DragDropFlags_AcceptNoDrawDefaultRect, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptNoDrawDefaultRect')
    DragDropFlags_AcceptNoDrawDefaultRect.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_AcceptNoDrawDefaultRect, 'cache'):
    DragDropFlags_AcceptNoDrawDefaultRect.cache = DragDropFlags_AcceptNoDrawDefaultRect.func()
  return DragDropFlags_AcceptNoDrawDefaultRect.cache

@reapy.inside_reaper()
def DragDropFlags_AcceptNoPreviewTooltip():
  if not hasattr(DragDropFlags_AcceptNoPreviewTooltip, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptNoPreviewTooltip')
    DragDropFlags_AcceptNoPreviewTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_AcceptNoPreviewTooltip, 'cache'):
    DragDropFlags_AcceptNoPreviewTooltip.cache = DragDropFlags_AcceptNoPreviewTooltip.func()
  return DragDropFlags_AcceptNoPreviewTooltip.cache

@reapy.inside_reaper()
def DragDropFlags_AcceptPeekOnly():
  if not hasattr(DragDropFlags_AcceptPeekOnly, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptPeekOnly')
    DragDropFlags_AcceptPeekOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_AcceptPeekOnly, 'cache'):
    DragDropFlags_AcceptPeekOnly.cache = DragDropFlags_AcceptPeekOnly.func()
  return DragDropFlags_AcceptPeekOnly.cache

@reapy.inside_reaper()
def DragDropFlags_None():
  if not hasattr(DragDropFlags_None, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_None')
    DragDropFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_None, 'cache'):
    DragDropFlags_None.cache = DragDropFlags_None.func()
  return DragDropFlags_None.cache

@reapy.inside_reaper()
def DragDropFlags_SourceAllowNullID():
  if not hasattr(DragDropFlags_SourceAllowNullID, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceAllowNullID')
    DragDropFlags_SourceAllowNullID.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_SourceAllowNullID, 'cache'):
    DragDropFlags_SourceAllowNullID.cache = DragDropFlags_SourceAllowNullID.func()
  return DragDropFlags_SourceAllowNullID.cache

@reapy.inside_reaper()
def DragDropFlags_SourceAutoExpirePayload():
  if not hasattr(DragDropFlags_SourceAutoExpirePayload, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceAutoExpirePayload')
    DragDropFlags_SourceAutoExpirePayload.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_SourceAutoExpirePayload, 'cache'):
    DragDropFlags_SourceAutoExpirePayload.cache = DragDropFlags_SourceAutoExpirePayload.func()
  return DragDropFlags_SourceAutoExpirePayload.cache

@reapy.inside_reaper()
def DragDropFlags_SourceExtern():
  if not hasattr(DragDropFlags_SourceExtern, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceExtern')
    DragDropFlags_SourceExtern.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_SourceExtern, 'cache'):
    DragDropFlags_SourceExtern.cache = DragDropFlags_SourceExtern.func()
  return DragDropFlags_SourceExtern.cache

@reapy.inside_reaper()
def DragDropFlags_SourceNoDisableHover():
  if not hasattr(DragDropFlags_SourceNoDisableHover, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceNoDisableHover')
    DragDropFlags_SourceNoDisableHover.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_SourceNoDisableHover, 'cache'):
    DragDropFlags_SourceNoDisableHover.cache = DragDropFlags_SourceNoDisableHover.func()
  return DragDropFlags_SourceNoDisableHover.cache

@reapy.inside_reaper()
def DragDropFlags_SourceNoHoldToOpenOthers():
  if not hasattr(DragDropFlags_SourceNoHoldToOpenOthers, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceNoHoldToOpenOthers')
    DragDropFlags_SourceNoHoldToOpenOthers.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_SourceNoHoldToOpenOthers, 'cache'):
    DragDropFlags_SourceNoHoldToOpenOthers.cache = DragDropFlags_SourceNoHoldToOpenOthers.func()
  return DragDropFlags_SourceNoHoldToOpenOthers.cache

@reapy.inside_reaper()
def DragDropFlags_SourceNoPreviewTooltip():
  if not hasattr(DragDropFlags_SourceNoPreviewTooltip, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceNoPreviewTooltip')
    DragDropFlags_SourceNoPreviewTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DragDropFlags_SourceNoPreviewTooltip, 'cache'):
    DragDropFlags_SourceNoPreviewTooltip.cache = DragDropFlags_SourceNoPreviewTooltip.func()
  return DragDropFlags_SourceNoPreviewTooltip.cache

@reapy.inside_reaper()
def DragFloatRange2(ctx, label, v_current_minInOut, v_current_maxInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, format_maxInOptional = None, flagsInOptional = None):
  if not hasattr(DragFloatRange2, 'func'):
    proc = rpr_getfp('ImGui_DragFloatRange2')
    DragFloatRange2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v_current_minInOut), c_double(v_current_maxInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, rpr_packsc(format_maxInOptional) if format_maxInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragFloatRange2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def DragInt(ctx, label, vInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragInt, 'func'):
    proc = rpr_getfp('ImGui_DragInt')
    DragInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(vInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragInt.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, args[6], byref(args[7]) if args[7] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def DragInt2(ctx, label, v1InOut, v2InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragInt2, 'func'):
    proc = rpr_getfp('ImGui_DragInt2')
    DragInt2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragInt2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], byref(args[8]) if args[8] != None else None)
  return rval, int(args[2].value), int(args[3].value)

@reapy.inside_reaper()
def DragInt3(ctx, label, v1InOut, v2InOut, v3InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragInt3, 'func'):
    proc = rpr_getfp('ImGui_DragInt3')
    DragInt3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragInt3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, args[8], byref(args[9]) if args[9] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value)

@reapy.inside_reaper()
def DragInt4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(DragInt4, 'func'):
    proc = rpr_getfp('ImGui_DragInt4')
    DragInt4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v4InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragInt4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None, args[9], byref(args[10]) if args[10] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

@reapy.inside_reaper()
def DragIntRange2(ctx, label, v_current_minInOut, v_current_maxInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, format_maxInOptional = None, flagsInOptional = None):
  if not hasattr(DragIntRange2, 'func'):
    proc = rpr_getfp('ImGui_DragIntRange2')
    DragIntRange2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v_current_minInOut), c_int(v_current_maxInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, rpr_packsc(format_maxInOptional) if format_maxInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = DragIntRange2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, int(args[2].value), int(args[3].value)

@reapy.inside_reaper()
def DrawFlags_Closed():
  if not hasattr(DrawFlags_Closed, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_Closed')
    DrawFlags_Closed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_Closed, 'cache'):
    DrawFlags_Closed.cache = DrawFlags_Closed.func()
  return DrawFlags_Closed.cache

@reapy.inside_reaper()
def DrawFlags_None():
  if not hasattr(DrawFlags_None, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_None')
    DrawFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_None, 'cache'):
    DrawFlags_None.cache = DrawFlags_None.func()
  return DrawFlags_None.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersAll():
  if not hasattr(DrawFlags_RoundCornersAll, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersAll')
    DrawFlags_RoundCornersAll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersAll, 'cache'):
    DrawFlags_RoundCornersAll.cache = DrawFlags_RoundCornersAll.func()
  return DrawFlags_RoundCornersAll.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersBottom():
  if not hasattr(DrawFlags_RoundCornersBottom, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersBottom')
    DrawFlags_RoundCornersBottom.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersBottom, 'cache'):
    DrawFlags_RoundCornersBottom.cache = DrawFlags_RoundCornersBottom.func()
  return DrawFlags_RoundCornersBottom.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersBottomLeft():
  if not hasattr(DrawFlags_RoundCornersBottomLeft, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersBottomLeft')
    DrawFlags_RoundCornersBottomLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersBottomLeft, 'cache'):
    DrawFlags_RoundCornersBottomLeft.cache = DrawFlags_RoundCornersBottomLeft.func()
  return DrawFlags_RoundCornersBottomLeft.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersBottomRight():
  if not hasattr(DrawFlags_RoundCornersBottomRight, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersBottomRight')
    DrawFlags_RoundCornersBottomRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersBottomRight, 'cache'):
    DrawFlags_RoundCornersBottomRight.cache = DrawFlags_RoundCornersBottomRight.func()
  return DrawFlags_RoundCornersBottomRight.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersLeft():
  if not hasattr(DrawFlags_RoundCornersLeft, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersLeft')
    DrawFlags_RoundCornersLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersLeft, 'cache'):
    DrawFlags_RoundCornersLeft.cache = DrawFlags_RoundCornersLeft.func()
  return DrawFlags_RoundCornersLeft.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersNone():
  if not hasattr(DrawFlags_RoundCornersNone, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersNone')
    DrawFlags_RoundCornersNone.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersNone, 'cache'):
    DrawFlags_RoundCornersNone.cache = DrawFlags_RoundCornersNone.func()
  return DrawFlags_RoundCornersNone.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersRight():
  if not hasattr(DrawFlags_RoundCornersRight, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersRight')
    DrawFlags_RoundCornersRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersRight, 'cache'):
    DrawFlags_RoundCornersRight.cache = DrawFlags_RoundCornersRight.func()
  return DrawFlags_RoundCornersRight.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersTop():
  if not hasattr(DrawFlags_RoundCornersTop, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersTop')
    DrawFlags_RoundCornersTop.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersTop, 'cache'):
    DrawFlags_RoundCornersTop.cache = DrawFlags_RoundCornersTop.func()
  return DrawFlags_RoundCornersTop.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersTopLeft():
  if not hasattr(DrawFlags_RoundCornersTopLeft, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersTopLeft')
    DrawFlags_RoundCornersTopLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersTopLeft, 'cache'):
    DrawFlags_RoundCornersTopLeft.cache = DrawFlags_RoundCornersTopLeft.func()
  return DrawFlags_RoundCornersTopLeft.cache

@reapy.inside_reaper()
def DrawFlags_RoundCornersTopRight():
  if not hasattr(DrawFlags_RoundCornersTopRight, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersTopRight')
    DrawFlags_RoundCornersTopRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(DrawFlags_RoundCornersTopRight, 'cache'):
    DrawFlags_RoundCornersTopRight.cache = DrawFlags_RoundCornersTopRight.func()
  return DrawFlags_RoundCornersTopRight.cache

@reapy.inside_reaper()
def DrawList_AddBezierCubic(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, col_rgba, thickness, num_segmentsInOptional = None):
  if not hasattr(DrawList_AddBezierCubic, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddBezierCubic')
    DrawList_AddBezierCubic.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(col_rgba), c_double(thickness), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  DrawList_AddBezierCubic.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10], byref(args[11]) if args[11] != None else None)

@reapy.inside_reaper()
def DrawList_AddBezierQuadratic(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, col_rgba, thickness, num_segmentsInOptional = None):
  if not hasattr(DrawList_AddBezierQuadratic, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddBezierQuadratic')
    DrawList_AddBezierQuadratic.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(col_rgba), c_double(thickness), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  DrawList_AddBezierQuadratic.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], byref(args[9]) if args[9] != None else None)

@reapy.inside_reaper()
def DrawList_AddCircle(draw_list, center_x, center_y, radius, col_rgba, num_segmentsInOptional = None, thicknessInOptional = None):
  if not hasattr(DrawList_AddCircle, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddCircle')
    DrawList_AddCircle.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None, c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_AddCircle.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)

@reapy.inside_reaper()
def DrawList_AddCircleFilled(draw_list, center_x, center_y, radius, col_rgba, num_segmentsInOptional = None):
  if not hasattr(DrawList_AddCircleFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddCircleFilled')
    DrawList_AddCircleFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  DrawList_AddCircleFilled.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)

@reapy.inside_reaper()
def DrawList_AddConvexPolyFilled(draw_list, points, num_points, col_rgba):
  if not hasattr(DrawList_AddConvexPolyFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddConvexPolyFilled')
    DrawList_AddConvexPolyFilled.func = CFUNCTYPE(None, c_void_p, c_void_p, c_int, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), rpr_packp('reaper_array*', points), c_int(num_points), c_int(col_rgba))
  DrawList_AddConvexPolyFilled.func(args[0], args[1], args[2], args[3])

@reapy.inside_reaper()
def DrawList_AddLine(draw_list, p1_x, p1_y, p2_x, p2_y, col_rgba, thicknessInOptional = None):
  if not hasattr(DrawList_AddLine, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddLine')
    DrawList_AddLine.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_int(col_rgba), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_AddLine.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)

@reapy.inside_reaper()
def DrawList_AddNgon(draw_list, center_x, center_y, radius, col_rgba, num_segments, thicknessInOptional = None):
  if not hasattr(DrawList_AddNgon, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddNgon')
    DrawList_AddNgon.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_int, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segments), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_AddNgon.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)

@reapy.inside_reaper()
def DrawList_AddNgonFilled(draw_list, center_x, center_y, radius, col_rgba, num_segments):
  if not hasattr(DrawList_AddNgonFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddNgonFilled')
    DrawList_AddNgonFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segments))
  DrawList_AddNgonFilled.func(args[0], args[1], args[2], args[3], args[4], args[5])

@reapy.inside_reaper()
def DrawList_AddPolyline(draw_list, points, col_rgba, flags, thickness):
  if not hasattr(DrawList_AddPolyline, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddPolyline')
    DrawList_AddPolyline.func = CFUNCTYPE(None, c_void_p, c_void_p, c_int, c_int, c_double)(proc)
  args = (rpr_packp('DrawList*', draw_list), rpr_packp('reaper_array*', points), c_int(col_rgba), c_int(flags), c_double(thickness))
  DrawList_AddPolyline.func(args[0], args[1], args[2], args[3], args[4])

@reapy.inside_reaper()
def DrawList_AddQuad(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, col_rgba, thicknessInOptional = None):
  if not hasattr(DrawList_AddQuad, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddQuad')
    DrawList_AddQuad.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(col_rgba), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_AddQuad.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], byref(args[10]) if args[10] != None else None)

@reapy.inside_reaper()
def DrawList_AddQuadFilled(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, col_rgba):
  if not hasattr(DrawList_AddQuadFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddQuadFilled')
    DrawList_AddQuadFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(col_rgba))
  DrawList_AddQuadFilled.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9])

@reapy.inside_reaper()
def DrawList_AddRect(draw_list, p_min_x, p_min_y, p_max_x, p_max_y, col_rgba, roundingInOptional = None, flagsInOptional = None, thicknessInOptional = None):
  if not hasattr(DrawList_AddRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddRect')
    DrawList_AddRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p_min_x), c_double(p_min_y), c_double(p_max_x), c_double(p_max_y), c_int(col_rgba), c_double(roundingInOptional) if roundingInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None, c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_AddRect.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None)

@reapy.inside_reaper()
def DrawList_AddRectFilled(draw_list, p_min_x, p_min_y, p_max_x, p_max_y, col_rgba, roundingInOptional = None, flagsInOptional = None):
  if not hasattr(DrawList_AddRectFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddRectFilled')
    DrawList_AddRectFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p_min_x), c_double(p_min_y), c_double(p_max_x), c_double(p_max_y), c_int(col_rgba), c_double(roundingInOptional) if roundingInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  DrawList_AddRectFilled.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None)

@reapy.inside_reaper()
def DrawList_AddRectFilledMultiColor(draw_list, p_min_x, p_min_y, p_max_x, p_max_y, col_upr_left, col_upr_right, col_bot_right, col_bot_left):
  if not hasattr(DrawList_AddRectFilledMultiColor, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddRectFilledMultiColor')
    DrawList_AddRectFilledMultiColor.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p_min_x), c_double(p_min_y), c_double(p_max_x), c_double(p_max_y), c_int(col_upr_left), c_int(col_upr_right), c_int(col_bot_right), c_int(col_bot_left))
  DrawList_AddRectFilledMultiColor.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])

@reapy.inside_reaper()
def DrawList_AddText(draw_list, x, y, col_rgba, text):
  if not hasattr(DrawList_AddText, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddText')
    DrawList_AddText.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_int, c_char_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(x), c_double(y), c_int(col_rgba), rpr_packsc(text))
  DrawList_AddText.func(args[0], args[1], args[2], args[3], args[4])

@reapy.inside_reaper()
def DrawList_AddTextEx(draw_list, font, font_size, pos_x, pos_y, col_rgba, text, wrap_widthInOptional = None, cpu_fine_clip_rect_xInOptional = None, cpu_fine_clip_rect_yInOptional = None, cpu_fine_clip_rect_wInOptional = None, cpu_fine_clip_rect_hInOptional = None):
  if not hasattr(DrawList_AddTextEx, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddTextEx')
    DrawList_AddTextEx.func = CFUNCTYPE(None, c_void_p, c_void_p, c_double, c_double, c_double, c_int, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), rpr_packp('Font*', font), c_double(font_size), c_double(pos_x), c_double(pos_y), c_int(col_rgba), rpr_packsc(text), c_double(wrap_widthInOptional) if wrap_widthInOptional != None else None, c_double(cpu_fine_clip_rect_xInOptional) if cpu_fine_clip_rect_xInOptional != None else None, c_double(cpu_fine_clip_rect_yInOptional) if cpu_fine_clip_rect_yInOptional != None else None, c_double(cpu_fine_clip_rect_wInOptional) if cpu_fine_clip_rect_wInOptional != None else None, c_double(cpu_fine_clip_rect_hInOptional) if cpu_fine_clip_rect_hInOptional != None else None)
  DrawList_AddTextEx.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None, byref(args[9]) if args[9] != None else None, byref(args[10]) if args[10] != None else None, byref(args[11]) if args[11] != None else None)

@reapy.inside_reaper()
def DrawList_AddTriangle(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, col_rgba, thicknessInOptional = None):
  if not hasattr(DrawList_AddTriangle, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddTriangle')
    DrawList_AddTriangle.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(col_rgba), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_AddTriangle.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)

@reapy.inside_reaper()
def DrawList_AddTriangleFilled(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, col_rgba):
  if not hasattr(DrawList_AddTriangleFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddTriangleFilled')
    DrawList_AddTriangleFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(col_rgba))
  DrawList_AddTriangleFilled.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

@reapy.inside_reaper()
def DrawList_PathArcTo(draw_list, center_x, center_y, radius, a_min, a_max, num_segmentsInOptional = None):
  if not hasattr(DrawList_PathArcTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathArcTo')
    DrawList_PathArcTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_double(a_min), c_double(a_max), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  DrawList_PathArcTo.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)

@reapy.inside_reaper()
def DrawList_PathArcToFast(draw_list, center_x, center_y, radius, a_min_of_12, a_max_of_12):
  if not hasattr(DrawList_PathArcToFast, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathArcToFast')
    DrawList_PathArcToFast.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(a_min_of_12), c_int(a_max_of_12))
  DrawList_PathArcToFast.func(args[0], args[1], args[2], args[3], args[4], args[5])

@reapy.inside_reaper()
def DrawList_PathBezierCubicCurveTo(draw_list, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, num_segmentsInOptional = None):
  if not hasattr(DrawList_PathBezierCubicCurveTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathBezierCubicCurveTo')
    DrawList_PathBezierCubicCurveTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  DrawList_PathBezierCubicCurveTo.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], byref(args[7]) if args[7] != None else None)

@reapy.inside_reaper()
def DrawList_PathBezierQuadraticCurveTo(draw_list, p2_x, p2_y, p3_x, p3_y, num_segmentsInOptional = None):
  if not hasattr(DrawList_PathBezierQuadraticCurveTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathBezierQuadraticCurveTo')
    DrawList_PathBezierQuadraticCurveTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  DrawList_PathBezierQuadraticCurveTo.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)

@reapy.inside_reaper()
def DrawList_PathClear(draw_list):
  if not hasattr(DrawList_PathClear, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathClear')
    DrawList_PathClear.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list),)
  DrawList_PathClear.func(args[0])

@reapy.inside_reaper()
def DrawList_PathFillConvex(draw_list, col_rgba):
  if not hasattr(DrawList_PathFillConvex, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathFillConvex')
    DrawList_PathFillConvex.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_int(col_rgba))
  DrawList_PathFillConvex.func(args[0], args[1])

@reapy.inside_reaper()
def DrawList_PathLineTo(draw_list, pos_x, pos_y):
  if not hasattr(DrawList_PathLineTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathLineTo')
    DrawList_PathLineTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(pos_x), c_double(pos_y))
  DrawList_PathLineTo.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def DrawList_PathRect(draw_list, rect_min_x, rect_min_y, rect_max_x, rect_max_y, roundingInOptional = None, flagsInOptional = None):
  if not hasattr(DrawList_PathRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathRect')
    DrawList_PathRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_void_p, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(rect_min_x), c_double(rect_min_y), c_double(rect_max_x), c_double(rect_max_y), c_double(roundingInOptional) if roundingInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  DrawList_PathRect.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)

@reapy.inside_reaper()
def DrawList_PathStroke(draw_list, col_rgba, flagsInOptional = None, thicknessInOptional = None):
  if not hasattr(DrawList_PathStroke, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathStroke')
    DrawList_PathStroke.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_int(col_rgba), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(thicknessInOptional) if thicknessInOptional != None else None)
  DrawList_PathStroke.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def DrawList_PopClipRect(draw_list):
  if not hasattr(DrawList_PopClipRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PopClipRect')
    DrawList_PopClipRect.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list),)
  DrawList_PopClipRect.func(args[0])

@reapy.inside_reaper()
def DrawList_PushClipRect(draw_list, clip_rect_min_x, clip_rect_min_y, clip_rect_max_x, clip_rect_max_y, intersect_with_current_clip_rectInOptional = None):
  if not hasattr(DrawList_PushClipRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PushClipRect')
    DrawList_PushClipRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list), c_double(clip_rect_min_x), c_double(clip_rect_min_y), c_double(clip_rect_max_x), c_double(clip_rect_max_y), c_bool(intersect_with_current_clip_rectInOptional) if intersect_with_current_clip_rectInOptional != None else None)
  DrawList_PushClipRect.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)

@reapy.inside_reaper()
def DrawList_PushClipRectFullScreen(draw_list):
  if not hasattr(DrawList_PushClipRectFullScreen, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PushClipRectFullScreen')
    DrawList_PushClipRectFullScreen.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('DrawList*', draw_list),)
  DrawList_PushClipRectFullScreen.func(args[0])

@reapy.inside_reaper()
def Dummy(ctx, size_w, size_h):
  if not hasattr(Dummy, 'func'):
    proc = rpr_getfp('ImGui_Dummy')
    Dummy.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(size_w), c_double(size_h))
  Dummy.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def End(ctx):
  if not hasattr(End, 'func'):
    proc = rpr_getfp('ImGui_End')
    End.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  End.func(args[0])

@reapy.inside_reaper()
def EndChild(ctx):
  if not hasattr(EndChild, 'func'):
    proc = rpr_getfp('ImGui_EndChild')
    EndChild.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndChild.func(args[0])

@reapy.inside_reaper()
def EndChildFrame(ctx):
  if not hasattr(EndChildFrame, 'func'):
    proc = rpr_getfp('ImGui_EndChildFrame')
    EndChildFrame.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndChildFrame.func(args[0])

@reapy.inside_reaper()
def EndCombo(ctx):
  if not hasattr(EndCombo, 'func'):
    proc = rpr_getfp('ImGui_EndCombo')
    EndCombo.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndCombo.func(args[0])

@reapy.inside_reaper()
def EndDisabled(ctx):
  if not hasattr(EndDisabled, 'func'):
    proc = rpr_getfp('ImGui_EndDisabled')
    EndDisabled.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndDisabled.func(args[0])

@reapy.inside_reaper()
def EndDragDropSource(ctx):
  if not hasattr(EndDragDropSource, 'func'):
    proc = rpr_getfp('ImGui_EndDragDropSource')
    EndDragDropSource.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndDragDropSource.func(args[0])

@reapy.inside_reaper()
def EndDragDropTarget(ctx):
  if not hasattr(EndDragDropTarget, 'func'):
    proc = rpr_getfp('ImGui_EndDragDropTarget')
    EndDragDropTarget.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndDragDropTarget.func(args[0])

@reapy.inside_reaper()
def EndGroup(ctx):
  if not hasattr(EndGroup, 'func'):
    proc = rpr_getfp('ImGui_EndGroup')
    EndGroup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndGroup.func(args[0])

@reapy.inside_reaper()
def EndListBox(ctx):
  if not hasattr(EndListBox, 'func'):
    proc = rpr_getfp('ImGui_EndListBox')
    EndListBox.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndListBox.func(args[0])

@reapy.inside_reaper()
def EndMenu(ctx):
  if not hasattr(EndMenu, 'func'):
    proc = rpr_getfp('ImGui_EndMenu')
    EndMenu.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndMenu.func(args[0])

@reapy.inside_reaper()
def EndMenuBar(ctx):
  if not hasattr(EndMenuBar, 'func'):
    proc = rpr_getfp('ImGui_EndMenuBar')
    EndMenuBar.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndMenuBar.func(args[0])

@reapy.inside_reaper()
def EndPopup(ctx):
  if not hasattr(EndPopup, 'func'):
    proc = rpr_getfp('ImGui_EndPopup')
    EndPopup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndPopup.func(args[0])

@reapy.inside_reaper()
def EndTabBar(ctx):
  if not hasattr(EndTabBar, 'func'):
    proc = rpr_getfp('ImGui_EndTabBar')
    EndTabBar.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndTabBar.func(args[0])

@reapy.inside_reaper()
def EndTabItem(ctx):
  if not hasattr(EndTabItem, 'func'):
    proc = rpr_getfp('ImGui_EndTabItem')
    EndTabItem.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndTabItem.func(args[0])

@reapy.inside_reaper()
def EndTable(ctx):
  if not hasattr(EndTable, 'func'):
    proc = rpr_getfp('ImGui_EndTable')
    EndTable.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndTable.func(args[0])

@reapy.inside_reaper()
def EndTooltip(ctx):
  if not hasattr(EndTooltip, 'func'):
    proc = rpr_getfp('ImGui_EndTooltip')
    EndTooltip.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  EndTooltip.func(args[0])

@reapy.inside_reaper()
def FocusedFlags_AnyWindow():
  if not hasattr(FocusedFlags_AnyWindow, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_AnyWindow')
    FocusedFlags_AnyWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_AnyWindow, 'cache'):
    FocusedFlags_AnyWindow.cache = FocusedFlags_AnyWindow.func()
  return FocusedFlags_AnyWindow.cache

@reapy.inside_reaper()
def FocusedFlags_ChildWindows():
  if not hasattr(FocusedFlags_ChildWindows, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_ChildWindows')
    FocusedFlags_ChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_ChildWindows, 'cache'):
    FocusedFlags_ChildWindows.cache = FocusedFlags_ChildWindows.func()
  return FocusedFlags_ChildWindows.cache

@reapy.inside_reaper()
def FocusedFlags_DockHierarchy():
  if not hasattr(FocusedFlags_DockHierarchy, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_DockHierarchy')
    FocusedFlags_DockHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_DockHierarchy, 'cache'):
    FocusedFlags_DockHierarchy.cache = FocusedFlags_DockHierarchy.func()
  return FocusedFlags_DockHierarchy.cache

@reapy.inside_reaper()
def FocusedFlags_NoPopupHierarchy():
  if not hasattr(FocusedFlags_NoPopupHierarchy, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_NoPopupHierarchy')
    FocusedFlags_NoPopupHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_NoPopupHierarchy, 'cache'):
    FocusedFlags_NoPopupHierarchy.cache = FocusedFlags_NoPopupHierarchy.func()
  return FocusedFlags_NoPopupHierarchy.cache

@reapy.inside_reaper()
def FocusedFlags_None():
  if not hasattr(FocusedFlags_None, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_None')
    FocusedFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_None, 'cache'):
    FocusedFlags_None.cache = FocusedFlags_None.func()
  return FocusedFlags_None.cache

@reapy.inside_reaper()
def FocusedFlags_RootAndChildWindows():
  if not hasattr(FocusedFlags_RootAndChildWindows, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_RootAndChildWindows')
    FocusedFlags_RootAndChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_RootAndChildWindows, 'cache'):
    FocusedFlags_RootAndChildWindows.cache = FocusedFlags_RootAndChildWindows.func()
  return FocusedFlags_RootAndChildWindows.cache

@reapy.inside_reaper()
def FocusedFlags_RootWindow():
  if not hasattr(FocusedFlags_RootWindow, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_RootWindow')
    FocusedFlags_RootWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FocusedFlags_RootWindow, 'cache'):
    FocusedFlags_RootWindow.cache = FocusedFlags_RootWindow.func()
  return FocusedFlags_RootWindow.cache

@reapy.inside_reaper()
def FontFlags_Bold():
  if not hasattr(FontFlags_Bold, 'func'):
    proc = rpr_getfp('ImGui_FontFlags_Bold')
    FontFlags_Bold.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FontFlags_Bold, 'cache'):
    FontFlags_Bold.cache = FontFlags_Bold.func()
  return FontFlags_Bold.cache

@reapy.inside_reaper()
def FontFlags_Italic():
  if not hasattr(FontFlags_Italic, 'func'):
    proc = rpr_getfp('ImGui_FontFlags_Italic')
    FontFlags_Italic.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FontFlags_Italic, 'cache'):
    FontFlags_Italic.cache = FontFlags_Italic.func()
  return FontFlags_Italic.cache

@reapy.inside_reaper()
def FontFlags_None():
  if not hasattr(FontFlags_None, 'func'):
    proc = rpr_getfp('ImGui_FontFlags_None')
    FontFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(FontFlags_None, 'cache'):
    FontFlags_None.cache = FontFlags_None.func()
  return FontFlags_None.cache

@reapy.inside_reaper()
def GetBackgroundDrawList(ctx):
  if not hasattr(GetBackgroundDrawList, 'func'):
    proc = rpr_getfp('ImGui_GetBackgroundDrawList')
    GetBackgroundDrawList.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetBackgroundDrawList.func(args[0])
  return rpr_unpackp('DrawList*', rval)

@reapy.inside_reaper()
def GetClipboardText(ctx):
  if not hasattr(GetClipboardText, 'func'):
    proc = rpr_getfp('ImGui_GetClipboardText')
    GetClipboardText.func = CFUNCTYPE(c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetClipboardText.func(args[0])
  return str(rval.decode())

@reapy.inside_reaper()
def GetColor(ctx, idx, alpha_mulInOptional = None):
  if not hasattr(GetColor, 'func'):
    proc = rpr_getfp('ImGui_GetColor')
    GetColor.func = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(idx), c_double(alpha_mulInOptional) if alpha_mulInOptional != None else None)
  rval = GetColor.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def GetColorEx(ctx, col_rgba):
  if not hasattr(GetColorEx, 'func'):
    proc = rpr_getfp('ImGui_GetColorEx')
    GetColorEx.func = CFUNCTYPE(c_int, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(col_rgba))
  rval = GetColorEx.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def GetConfigFlags(ctx):
  if not hasattr(GetConfigFlags, 'func'):
    proc = rpr_getfp('ImGui_GetConfigFlags')
    GetConfigFlags.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetConfigFlags.func(args[0])
  return rval

@reapy.inside_reaper()
def GetContentRegionAvail(ctx, xOut = None, yOut = None):
  if not hasattr(GetContentRegionAvail, 'func'):
    proc = rpr_getfp('ImGui_GetContentRegionAvail')
    GetContentRegionAvail.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetContentRegionAvail.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetContentRegionMax(ctx, xOut = None, yOut = None):
  if not hasattr(GetContentRegionMax, 'func'):
    proc = rpr_getfp('ImGui_GetContentRegionMax')
    GetContentRegionMax.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetContentRegionMax.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetCursorPos(ctx, xOut = None, yOut = None):
  if not hasattr(GetCursorPos, 'func'):
    proc = rpr_getfp('ImGui_GetCursorPos')
    GetCursorPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetCursorPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetCursorPosX(ctx):
  if not hasattr(GetCursorPosX, 'func'):
    proc = rpr_getfp('ImGui_GetCursorPosX')
    GetCursorPosX.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetCursorPosX.func(args[0])
  return rval

@reapy.inside_reaper()
def GetCursorPosY(ctx):
  if not hasattr(GetCursorPosY, 'func'):
    proc = rpr_getfp('ImGui_GetCursorPosY')
    GetCursorPosY.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetCursorPosY.func(args[0])
  return rval

@reapy.inside_reaper()
def GetCursorScreenPos(ctx, xOut = None, yOut = None):
  if not hasattr(GetCursorScreenPos, 'func'):
    proc = rpr_getfp('ImGui_GetCursorScreenPos')
    GetCursorScreenPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetCursorScreenPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetCursorStartPos(ctx, xOut = None, yOut = None):
  if not hasattr(GetCursorStartPos, 'func'):
    proc = rpr_getfp('ImGui_GetCursorStartPos')
    GetCursorStartPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetCursorStartPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetDeltaTime(ctx):
  if not hasattr(GetDeltaTime, 'func'):
    proc = rpr_getfp('ImGui_GetDeltaTime')
    GetDeltaTime.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetDeltaTime.func(args[0])
  return rval

@reapy.inside_reaper()
def GetDragDropPayload(ctx, typeOut = None, typeOut_sz = None, payloadOutNeedBig = None, payloadOutNeedBig_sz = None, is_previewOut = None, is_deliveryOut = None):
  if not hasattr(GetDragDropPayload, 'func'):
    proc = rpr_getfp('ImGui_GetDragDropPayload')
    GetDragDropPayload.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int, c_char_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packs(typeOut if typeOut != None else 0), c_int(typeOut_sz if typeOut_sz != None else 0), rpr_packs(payloadOutNeedBig if payloadOutNeedBig != None else 0), c_int(payloadOutNeedBig_sz if payloadOutNeedBig_sz != None else 0), c_bool(is_previewOut if is_previewOut != None else 0), c_bool(is_deliveryOut if is_deliveryOut != None else 0))
  rval = GetDragDropPayload.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]), byref(args[6]))
  return rval, rpr_unpacks(args[1]), rpr_unpacks(args[3]), int(args[5].value), int(args[6].value)

@reapy.inside_reaper()
def GetDragDropPayloadFile(ctx, index, filenameOut = None, filenameOut_sz = None):
  if not hasattr(GetDragDropPayloadFile, 'func'):
    proc = rpr_getfp('ImGui_GetDragDropPayloadFile')
    GetDragDropPayloadFile.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_char_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(index), rpr_packs(filenameOut if filenameOut != None else 0), c_int(filenameOut_sz if filenameOut_sz != None else 0))
  rval = GetDragDropPayloadFile.func(args[0], args[1], args[2], args[3])
  return rval, rpr_unpacks(args[2])

@reapy.inside_reaper()
def GetFont(ctx):
  if not hasattr(GetFont, 'func'):
    proc = rpr_getfp('ImGui_GetFont')
    GetFont.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetFont.func(args[0])
  return rpr_unpackp('Font*', rval)

@reapy.inside_reaper()
def GetFontSize(ctx):
  if not hasattr(GetFontSize, 'func'):
    proc = rpr_getfp('ImGui_GetFontSize')
    GetFontSize.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetFontSize.func(args[0])
  return rval

@reapy.inside_reaper()
def GetForegroundDrawList(ctx):
  if not hasattr(GetForegroundDrawList, 'func'):
    proc = rpr_getfp('ImGui_GetForegroundDrawList')
    GetForegroundDrawList.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetForegroundDrawList.func(args[0])
  return rpr_unpackp('DrawList*', rval)

@reapy.inside_reaper()
def GetFrameCount(ctx):
  if not hasattr(GetFrameCount, 'func'):
    proc = rpr_getfp('ImGui_GetFrameCount')
    GetFrameCount.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetFrameCount.func(args[0])
  return rval

@reapy.inside_reaper()
def GetFrameHeight(ctx):
  if not hasattr(GetFrameHeight, 'func'):
    proc = rpr_getfp('ImGui_GetFrameHeight')
    GetFrameHeight.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetFrameHeight.func(args[0])
  return rval

@reapy.inside_reaper()
def GetFrameHeightWithSpacing(ctx):
  if not hasattr(GetFrameHeightWithSpacing, 'func'):
    proc = rpr_getfp('ImGui_GetFrameHeightWithSpacing')
    GetFrameHeightWithSpacing.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetFrameHeightWithSpacing.func(args[0])
  return rval

@reapy.inside_reaper()
def GetInputQueueCharacter(ctx, idx, unicode_charOut = None):
  if not hasattr(GetInputQueueCharacter, 'func'):
    proc = rpr_getfp('ImGui_GetInputQueueCharacter')
    GetInputQueueCharacter.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(idx), c_int(unicode_charOut if unicode_charOut != None else 0))
  rval = GetInputQueueCharacter.func(args[0], args[1], byref(args[2]))
  return rval, int(args[2].value)

@reapy.inside_reaper()
def GetItemRectMax(ctx, xOut = None, yOut = None):
  if not hasattr(GetItemRectMax, 'func'):
    proc = rpr_getfp('ImGui_GetItemRectMax')
    GetItemRectMax.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetItemRectMax.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetItemRectMin(ctx, xOut = None, yOut = None):
  if not hasattr(GetItemRectMin, 'func'):
    proc = rpr_getfp('ImGui_GetItemRectMin')
    GetItemRectMin.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetItemRectMin.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetItemRectSize(ctx, wOut = None, hOut = None):
  if not hasattr(GetItemRectSize, 'func'):
    proc = rpr_getfp('ImGui_GetItemRectSize')
    GetItemRectSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(wOut if wOut != None else 0), c_double(hOut if hOut != None else 0))
  GetItemRectSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetKeyDownDuration(ctx, key_code):
  if not hasattr(GetKeyDownDuration, 'func'):
    proc = rpr_getfp('ImGui_GetKeyDownDuration')
    GetKeyDownDuration.func = CFUNCTYPE(c_double, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(key_code))
  rval = GetKeyDownDuration.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def GetKeyMods(ctx):
  if not hasattr(GetKeyMods, 'func'):
    proc = rpr_getfp('ImGui_GetKeyMods')
    GetKeyMods.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetKeyMods.func(args[0])
  return rval

@reapy.inside_reaper()
def GetKeyPressedAmount(ctx, key_index, repeat_delay, rate):
  if not hasattr(GetKeyPressedAmount, 'func'):
    proc = rpr_getfp('ImGui_GetKeyPressedAmount')
    GetKeyPressedAmount.func = CFUNCTYPE(c_int, c_void_p, c_int, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_int(key_index), c_double(repeat_delay), c_double(rate))
  rval = GetKeyPressedAmount.func(args[0], args[1], args[2], args[3])
  return rval

@reapy.inside_reaper()
def GetMainViewport(ctx):
  if not hasattr(GetMainViewport, 'func'):
    proc = rpr_getfp('ImGui_GetMainViewport')
    GetMainViewport.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetMainViewport.func(args[0])
  return rpr_unpackp('Viewport*', rval)

@reapy.inside_reaper()
def GetMouseClickedPos(ctx, button, xOut = None, yOut = None):
  if not hasattr(GetMouseClickedPos, 'func'):
    proc = rpr_getfp('ImGui_GetMouseClickedPos')
    GetMouseClickedPos.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetMouseClickedPos.func(args[0], args[1], byref(args[2]), byref(args[3]))
  return float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def GetMouseCursor(ctx):
  if not hasattr(GetMouseCursor, 'func'):
    proc = rpr_getfp('ImGui_GetMouseCursor')
    GetMouseCursor.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetMouseCursor.func(args[0])
  return rval

@reapy.inside_reaper()
def GetMouseDelta(ctx, xOut = None, yOut = None):
  if not hasattr(GetMouseDelta, 'func'):
    proc = rpr_getfp('ImGui_GetMouseDelta')
    GetMouseDelta.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetMouseDelta.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetMouseDownDuration(ctx, button):
  if not hasattr(GetMouseDownDuration, 'func'):
    proc = rpr_getfp('ImGui_GetMouseDownDuration')
    GetMouseDownDuration.func = CFUNCTYPE(c_double, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button))
  rval = GetMouseDownDuration.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def GetMouseDragDelta(ctx, xOut = None, yOut = None, buttonInOptional = None, lock_thresholdInOptional = None):
  if not hasattr(GetMouseDragDelta, 'func'):
    proc = rpr_getfp('ImGui_GetMouseDragDelta')
    GetMouseDragDelta.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0), c_int(buttonInOptional) if buttonInOptional != None else None, c_double(lock_thresholdInOptional) if lock_thresholdInOptional != None else None)
  GetMouseDragDelta.func(args[0], byref(args[1]), byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetMousePos(ctx, xOut = None, yOut = None):
  if not hasattr(GetMousePos, 'func'):
    proc = rpr_getfp('ImGui_GetMousePos')
    GetMousePos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetMousePos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetMousePosOnOpeningCurrentPopup(ctx, xOut = None, yOut = None):
  if not hasattr(GetMousePosOnOpeningCurrentPopup, 'func'):
    proc = rpr_getfp('ImGui_GetMousePosOnOpeningCurrentPopup')
    GetMousePosOnOpeningCurrentPopup.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetMousePosOnOpeningCurrentPopup.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetMouseWheel(ctx, verticalOut = None, horizontalOut = None):
  if not hasattr(GetMouseWheel, 'func'):
    proc = rpr_getfp('ImGui_GetMouseWheel')
    GetMouseWheel.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(verticalOut if verticalOut != None else 0), c_double(horizontalOut if horizontalOut != None else 0))
  GetMouseWheel.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetScrollMaxX(ctx):
  if not hasattr(GetScrollMaxX, 'func'):
    proc = rpr_getfp('ImGui_GetScrollMaxX')
    GetScrollMaxX.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetScrollMaxX.func(args[0])
  return rval

@reapy.inside_reaper()
def GetScrollMaxY(ctx):
  if not hasattr(GetScrollMaxY, 'func'):
    proc = rpr_getfp('ImGui_GetScrollMaxY')
    GetScrollMaxY.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetScrollMaxY.func(args[0])
  return rval

@reapy.inside_reaper()
def GetScrollX(ctx):
  if not hasattr(GetScrollX, 'func'):
    proc = rpr_getfp('ImGui_GetScrollX')
    GetScrollX.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetScrollX.func(args[0])
  return rval

@reapy.inside_reaper()
def GetScrollY(ctx):
  if not hasattr(GetScrollY, 'func'):
    proc = rpr_getfp('ImGui_GetScrollY')
    GetScrollY.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetScrollY.func(args[0])
  return rval

@reapy.inside_reaper()
def GetStyleColor(ctx, idx):
  if not hasattr(GetStyleColor, 'func'):
    proc = rpr_getfp('ImGui_GetStyleColor')
    GetStyleColor.func = CFUNCTYPE(c_int, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(idx))
  rval = GetStyleColor.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def GetStyleColorName(idx):
  if not hasattr(GetStyleColorName, 'func'):
    proc = rpr_getfp('ImGui_GetStyleColorName')
    GetStyleColorName.func = CFUNCTYPE(c_char_p, c_int)(proc)
  args = (c_int(idx),)
  rval = GetStyleColorName.func(args[0])
  return str(rval.decode())

@reapy.inside_reaper()
def GetStyleVar(ctx, var_idx, val1Out = None, val2Out = None):
  if not hasattr(GetStyleVar, 'func'):
    proc = rpr_getfp('ImGui_GetStyleVar')
    GetStyleVar.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(var_idx), c_double(val1Out if val1Out != None else 0), c_double(val2Out if val2Out != None else 0))
  GetStyleVar.func(args[0], args[1], byref(args[2]), byref(args[3]))
  return float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def GetTextLineHeight(ctx):
  if not hasattr(GetTextLineHeight, 'func'):
    proc = rpr_getfp('ImGui_GetTextLineHeight')
    GetTextLineHeight.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetTextLineHeight.func(args[0])
  return rval

@reapy.inside_reaper()
def GetTextLineHeightWithSpacing(ctx):
  if not hasattr(GetTextLineHeightWithSpacing, 'func'):
    proc = rpr_getfp('ImGui_GetTextLineHeightWithSpacing')
    GetTextLineHeightWithSpacing.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetTextLineHeightWithSpacing.func(args[0])
  return rval

@reapy.inside_reaper()
def GetTime(ctx):
  if not hasattr(GetTime, 'func'):
    proc = rpr_getfp('ImGui_GetTime')
    GetTime.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetTime.func(args[0])
  return rval

@reapy.inside_reaper()
def GetTreeNodeToLabelSpacing(ctx):
  if not hasattr(GetTreeNodeToLabelSpacing, 'func'):
    proc = rpr_getfp('ImGui_GetTreeNodeToLabelSpacing')
    GetTreeNodeToLabelSpacing.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetTreeNodeToLabelSpacing.func(args[0])
  return rval

@reapy.inside_reaper()
def GetVersion(imgui_versionOut = None, imgui_versionOut_sz = None, reaimgui_versionOut = None, reaimgui_versionOut_sz = None):
  if not hasattr(GetVersion, 'func'):
    proc = rpr_getfp('ImGui_GetVersion')
    GetVersion.func = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int)(proc)
  args = (rpr_packs(imgui_versionOut if imgui_versionOut != None else 0), c_int(imgui_versionOut_sz if imgui_versionOut_sz != None else 0), rpr_packs(reaimgui_versionOut if reaimgui_versionOut != None else 0), c_int(reaimgui_versionOut_sz if reaimgui_versionOut_sz != None else 0))
  GetVersion.func(args[0], args[1], args[2], args[3])
  return rpr_unpacks(args[0]), rpr_unpacks(args[2])

@reapy.inside_reaper()
def GetWindowContentRegionMax(ctx, xOut = None, yOut = None):
  if not hasattr(GetWindowContentRegionMax, 'func'):
    proc = rpr_getfp('ImGui_GetWindowContentRegionMax')
    GetWindowContentRegionMax.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetWindowContentRegionMax.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetWindowContentRegionMin(ctx, xOut = None, yOut = None):
  if not hasattr(GetWindowContentRegionMin, 'func'):
    proc = rpr_getfp('ImGui_GetWindowContentRegionMin')
    GetWindowContentRegionMin.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetWindowContentRegionMin.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetWindowDockID(ctx):
  if not hasattr(GetWindowDockID, 'func'):
    proc = rpr_getfp('ImGui_GetWindowDockID')
    GetWindowDockID.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetWindowDockID.func(args[0])
  return rval

@reapy.inside_reaper()
def GetWindowDrawList(ctx):
  if not hasattr(GetWindowDrawList, 'func'):
    proc = rpr_getfp('ImGui_GetWindowDrawList')
    GetWindowDrawList.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetWindowDrawList.func(args[0])
  return rpr_unpackp('DrawList*', rval)

@reapy.inside_reaper()
def GetWindowHeight(ctx):
  if not hasattr(GetWindowHeight, 'func'):
    proc = rpr_getfp('ImGui_GetWindowHeight')
    GetWindowHeight.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetWindowHeight.func(args[0])
  return rval

@reapy.inside_reaper()
def GetWindowPos(ctx, xOut = None, yOut = None):
  if not hasattr(GetWindowPos, 'func'):
    proc = rpr_getfp('ImGui_GetWindowPos')
    GetWindowPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  GetWindowPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetWindowSize(ctx, wOut = None, hOut = None):
  if not hasattr(GetWindowSize, 'func'):
    proc = rpr_getfp('ImGui_GetWindowSize')
    GetWindowSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(wOut if wOut != None else 0), c_double(hOut if hOut != None else 0))
  GetWindowSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def GetWindowWidth(ctx):
  if not hasattr(GetWindowWidth, 'func'):
    proc = rpr_getfp('ImGui_GetWindowWidth')
    GetWindowWidth.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = GetWindowWidth.func(args[0])
  return rval

@reapy.inside_reaper()
def HoveredFlags_AllowWhenBlockedByActiveItem():
  if not hasattr(HoveredFlags_AllowWhenBlockedByActiveItem, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenBlockedByActiveItem')
    HoveredFlags_AllowWhenBlockedByActiveItem.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_AllowWhenBlockedByActiveItem, 'cache'):
    HoveredFlags_AllowWhenBlockedByActiveItem.cache = HoveredFlags_AllowWhenBlockedByActiveItem.func()
  return HoveredFlags_AllowWhenBlockedByActiveItem.cache

@reapy.inside_reaper()
def HoveredFlags_AllowWhenBlockedByPopup():
  if not hasattr(HoveredFlags_AllowWhenBlockedByPopup, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenBlockedByPopup')
    HoveredFlags_AllowWhenBlockedByPopup.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_AllowWhenBlockedByPopup, 'cache'):
    HoveredFlags_AllowWhenBlockedByPopup.cache = HoveredFlags_AllowWhenBlockedByPopup.func()
  return HoveredFlags_AllowWhenBlockedByPopup.cache

@reapy.inside_reaper()
def HoveredFlags_AllowWhenDisabled():
  if not hasattr(HoveredFlags_AllowWhenDisabled, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenDisabled')
    HoveredFlags_AllowWhenDisabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_AllowWhenDisabled, 'cache'):
    HoveredFlags_AllowWhenDisabled.cache = HoveredFlags_AllowWhenDisabled.func()
  return HoveredFlags_AllowWhenDisabled.cache

@reapy.inside_reaper()
def HoveredFlags_AllowWhenOverlapped():
  if not hasattr(HoveredFlags_AllowWhenOverlapped, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenOverlapped')
    HoveredFlags_AllowWhenOverlapped.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_AllowWhenOverlapped, 'cache'):
    HoveredFlags_AllowWhenOverlapped.cache = HoveredFlags_AllowWhenOverlapped.func()
  return HoveredFlags_AllowWhenOverlapped.cache

@reapy.inside_reaper()
def HoveredFlags_AnyWindow():
  if not hasattr(HoveredFlags_AnyWindow, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AnyWindow')
    HoveredFlags_AnyWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_AnyWindow, 'cache'):
    HoveredFlags_AnyWindow.cache = HoveredFlags_AnyWindow.func()
  return HoveredFlags_AnyWindow.cache

@reapy.inside_reaper()
def HoveredFlags_ChildWindows():
  if not hasattr(HoveredFlags_ChildWindows, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_ChildWindows')
    HoveredFlags_ChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_ChildWindows, 'cache'):
    HoveredFlags_ChildWindows.cache = HoveredFlags_ChildWindows.func()
  return HoveredFlags_ChildWindows.cache

@reapy.inside_reaper()
def HoveredFlags_DockHierarchy():
  if not hasattr(HoveredFlags_DockHierarchy, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_DockHierarchy')
    HoveredFlags_DockHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_DockHierarchy, 'cache'):
    HoveredFlags_DockHierarchy.cache = HoveredFlags_DockHierarchy.func()
  return HoveredFlags_DockHierarchy.cache

@reapy.inside_reaper()
def HoveredFlags_NoPopupHierarchy():
  if not hasattr(HoveredFlags_NoPopupHierarchy, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_NoPopupHierarchy')
    HoveredFlags_NoPopupHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_NoPopupHierarchy, 'cache'):
    HoveredFlags_NoPopupHierarchy.cache = HoveredFlags_NoPopupHierarchy.func()
  return HoveredFlags_NoPopupHierarchy.cache

@reapy.inside_reaper()
def HoveredFlags_None():
  if not hasattr(HoveredFlags_None, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_None')
    HoveredFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_None, 'cache'):
    HoveredFlags_None.cache = HoveredFlags_None.func()
  return HoveredFlags_None.cache

@reapy.inside_reaper()
def HoveredFlags_RectOnly():
  if not hasattr(HoveredFlags_RectOnly, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_RectOnly')
    HoveredFlags_RectOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_RectOnly, 'cache'):
    HoveredFlags_RectOnly.cache = HoveredFlags_RectOnly.func()
  return HoveredFlags_RectOnly.cache

@reapy.inside_reaper()
def HoveredFlags_RootAndChildWindows():
  if not hasattr(HoveredFlags_RootAndChildWindows, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_RootAndChildWindows')
    HoveredFlags_RootAndChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_RootAndChildWindows, 'cache'):
    HoveredFlags_RootAndChildWindows.cache = HoveredFlags_RootAndChildWindows.func()
  return HoveredFlags_RootAndChildWindows.cache

@reapy.inside_reaper()
def HoveredFlags_RootWindow():
  if not hasattr(HoveredFlags_RootWindow, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_RootWindow')
    HoveredFlags_RootWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(HoveredFlags_RootWindow, 'cache'):
    HoveredFlags_RootWindow.cache = HoveredFlags_RootWindow.func()
  return HoveredFlags_RootWindow.cache

@reapy.inside_reaper()
def Indent(ctx, indent_wInOptional = None):
  if not hasattr(Indent, 'func'):
    proc = rpr_getfp('ImGui_Indent')
    Indent.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(indent_wInOptional) if indent_wInOptional != None else None)
  Indent.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def InputDouble(ctx, label, vInOut, stepInOptional = None, step_fastInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(InputDouble, 'func'):
    proc = rpr_getfp('ImGui_InputDouble')
    InputDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(vInOut), c_double(stepInOptional) if stepInOptional != None else None, c_double(step_fastInOptional) if step_fastInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputDouble.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value)

@reapy.inside_reaper()
def InputDouble2(ctx, label, v1InOut, v2InOut, formatInOptional = None, flagsInOptional = None):
  if not hasattr(InputDouble2, 'func'):
    proc = rpr_getfp('ImGui_InputDouble2')
    InputDouble2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputDouble2.func(args[0], args[1], byref(args[2]), byref(args[3]), args[4], byref(args[5]) if args[5] != None else None)
  return rval, float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def InputDouble3(ctx, label, v1InOut, v2InOut, v3InOut, formatInOptional = None, flagsInOptional = None):
  if not hasattr(InputDouble3, 'func'):
    proc = rpr_getfp('ImGui_InputDouble3')
    InputDouble3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputDouble3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value)

@reapy.inside_reaper()
def InputDouble4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, formatInOptional = None, flagsInOptional = None):
  if not hasattr(InputDouble4, 'func'):
    proc = rpr_getfp('ImGui_InputDouble4')
    InputDouble4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v4InOut), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputDouble4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), args[6], byref(args[7]) if args[7] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value), float(args[5].value)

@reapy.inside_reaper()
def InputDoubleN(ctx, label, values, stepInOptional = None, step_fastInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(InputDoubleN, 'func'):
    proc = rpr_getfp('ImGui_InputDoubleN')
    InputDoubleN.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_double(stepInOptional) if stepInOptional != None else None, c_double(step_fastInOptional) if step_fastInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputDoubleN.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, args[5], byref(args[6]) if args[6] != None else None)
  return rval

@reapy.inside_reaper()
def InputInt(ctx, label, vInOut, stepInOptional = None, step_fastInOptional = None, flagsInOptional = None):
  if not hasattr(InputInt, 'func'):
    proc = rpr_getfp('ImGui_InputInt')
    InputInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(vInOut), c_int(stepInOptional) if stepInOptional != None else None, c_int(step_fastInOptional) if step_fastInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputInt.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def InputInt2(ctx, label, v1InOut, v2InOut, flagsInOptional = None):
  if not hasattr(InputInt2, 'func'):
    proc = rpr_getfp('ImGui_InputInt2')
    InputInt2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputInt2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None)
  return rval, int(args[2].value), int(args[3].value)

@reapy.inside_reaper()
def InputInt3(ctx, label, v1InOut, v2InOut, v3InOut, flagsInOptional = None):
  if not hasattr(InputInt3, 'func'):
    proc = rpr_getfp('ImGui_InputInt3')
    InputInt3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputInt3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value)

@reapy.inside_reaper()
def InputInt4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, flagsInOptional = None):
  if not hasattr(InputInt4, 'func'):
    proc = rpr_getfp('ImGui_InputInt4')
    InputInt4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v4InOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputInt4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), byref(args[6]) if args[6] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

@reapy.inside_reaper()
def InputText(ctx, label, bufInOutNeedBig, bufInOutNeedBig_sz, flagsInOptional = None):
  if not hasattr(InputText, 'func'):
    proc = rpr_getfp('ImGui_InputText')
    InputText.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packs(bufInOutNeedBig), c_int(bufInOutNeedBig_sz), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputText.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval, rpr_unpacks(args[2])

@reapy.inside_reaper()
def InputTextFlags_AllowTabInput():
  if not hasattr(InputTextFlags_AllowTabInput, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_AllowTabInput')
    InputTextFlags_AllowTabInput.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_AllowTabInput, 'cache'):
    InputTextFlags_AllowTabInput.cache = InputTextFlags_AllowTabInput.func()
  return InputTextFlags_AllowTabInput.cache

@reapy.inside_reaper()
def InputTextFlags_AlwaysOverwrite():
  if not hasattr(InputTextFlags_AlwaysOverwrite, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_AlwaysOverwrite')
    InputTextFlags_AlwaysOverwrite.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_AlwaysOverwrite, 'cache'):
    InputTextFlags_AlwaysOverwrite.cache = InputTextFlags_AlwaysOverwrite.func()
  return InputTextFlags_AlwaysOverwrite.cache

@reapy.inside_reaper()
def InputTextFlags_AutoSelectAll():
  if not hasattr(InputTextFlags_AutoSelectAll, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_AutoSelectAll')
    InputTextFlags_AutoSelectAll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_AutoSelectAll, 'cache'):
    InputTextFlags_AutoSelectAll.cache = InputTextFlags_AutoSelectAll.func()
  return InputTextFlags_AutoSelectAll.cache

@reapy.inside_reaper()
def InputTextFlags_CharsDecimal():
  if not hasattr(InputTextFlags_CharsDecimal, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsDecimal')
    InputTextFlags_CharsDecimal.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_CharsDecimal, 'cache'):
    InputTextFlags_CharsDecimal.cache = InputTextFlags_CharsDecimal.func()
  return InputTextFlags_CharsDecimal.cache

@reapy.inside_reaper()
def InputTextFlags_CharsHexadecimal():
  if not hasattr(InputTextFlags_CharsHexadecimal, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsHexadecimal')
    InputTextFlags_CharsHexadecimal.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_CharsHexadecimal, 'cache'):
    InputTextFlags_CharsHexadecimal.cache = InputTextFlags_CharsHexadecimal.func()
  return InputTextFlags_CharsHexadecimal.cache

@reapy.inside_reaper()
def InputTextFlags_CharsNoBlank():
  if not hasattr(InputTextFlags_CharsNoBlank, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsNoBlank')
    InputTextFlags_CharsNoBlank.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_CharsNoBlank, 'cache'):
    InputTextFlags_CharsNoBlank.cache = InputTextFlags_CharsNoBlank.func()
  return InputTextFlags_CharsNoBlank.cache

@reapy.inside_reaper()
def InputTextFlags_CharsScientific():
  if not hasattr(InputTextFlags_CharsScientific, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsScientific')
    InputTextFlags_CharsScientific.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_CharsScientific, 'cache'):
    InputTextFlags_CharsScientific.cache = InputTextFlags_CharsScientific.func()
  return InputTextFlags_CharsScientific.cache

@reapy.inside_reaper()
def InputTextFlags_CharsUppercase():
  if not hasattr(InputTextFlags_CharsUppercase, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsUppercase')
    InputTextFlags_CharsUppercase.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_CharsUppercase, 'cache'):
    InputTextFlags_CharsUppercase.cache = InputTextFlags_CharsUppercase.func()
  return InputTextFlags_CharsUppercase.cache

@reapy.inside_reaper()
def InputTextFlags_CtrlEnterForNewLine():
  if not hasattr(InputTextFlags_CtrlEnterForNewLine, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CtrlEnterForNewLine')
    InputTextFlags_CtrlEnterForNewLine.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_CtrlEnterForNewLine, 'cache'):
    InputTextFlags_CtrlEnterForNewLine.cache = InputTextFlags_CtrlEnterForNewLine.func()
  return InputTextFlags_CtrlEnterForNewLine.cache

@reapy.inside_reaper()
def InputTextFlags_EnterReturnsTrue():
  if not hasattr(InputTextFlags_EnterReturnsTrue, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_EnterReturnsTrue')
    InputTextFlags_EnterReturnsTrue.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_EnterReturnsTrue, 'cache'):
    InputTextFlags_EnterReturnsTrue.cache = InputTextFlags_EnterReturnsTrue.func()
  return InputTextFlags_EnterReturnsTrue.cache

@reapy.inside_reaper()
def InputTextFlags_NoHorizontalScroll():
  if not hasattr(InputTextFlags_NoHorizontalScroll, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_NoHorizontalScroll')
    InputTextFlags_NoHorizontalScroll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_NoHorizontalScroll, 'cache'):
    InputTextFlags_NoHorizontalScroll.cache = InputTextFlags_NoHorizontalScroll.func()
  return InputTextFlags_NoHorizontalScroll.cache

@reapy.inside_reaper()
def InputTextFlags_NoUndoRedo():
  if not hasattr(InputTextFlags_NoUndoRedo, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_NoUndoRedo')
    InputTextFlags_NoUndoRedo.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_NoUndoRedo, 'cache'):
    InputTextFlags_NoUndoRedo.cache = InputTextFlags_NoUndoRedo.func()
  return InputTextFlags_NoUndoRedo.cache

@reapy.inside_reaper()
def InputTextFlags_None():
  if not hasattr(InputTextFlags_None, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_None')
    InputTextFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_None, 'cache'):
    InputTextFlags_None.cache = InputTextFlags_None.func()
  return InputTextFlags_None.cache

@reapy.inside_reaper()
def InputTextFlags_Password():
  if not hasattr(InputTextFlags_Password, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_Password')
    InputTextFlags_Password.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_Password, 'cache'):
    InputTextFlags_Password.cache = InputTextFlags_Password.func()
  return InputTextFlags_Password.cache

@reapy.inside_reaper()
def InputTextFlags_ReadOnly():
  if not hasattr(InputTextFlags_ReadOnly, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_ReadOnly')
    InputTextFlags_ReadOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(InputTextFlags_ReadOnly, 'cache'):
    InputTextFlags_ReadOnly.cache = InputTextFlags_ReadOnly.func()
  return InputTextFlags_ReadOnly.cache

@reapy.inside_reaper()
def InputTextMultiline(ctx, label, bufInOutNeedBig, bufInOutNeedBig_sz, size_wInOptional = None, size_hInOptional = None, flagsInOptional = None):
  if not hasattr(InputTextMultiline, 'func'):
    proc = rpr_getfp('ImGui_InputTextMultiline')
    InputTextMultiline.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_int, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packs(bufInOutNeedBig), c_int(bufInOutNeedBig_sz), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputTextMultiline.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)
  return rval, rpr_unpacks(args[2])

@reapy.inside_reaper()
def InputTextWithHint(ctx, label, hint, bufInOutNeedBig, bufInOutNeedBig_sz, flagsInOptional = None):
  if not hasattr(InputTextWithHint, 'func'):
    proc = rpr_getfp('ImGui_InputTextWithHint')
    InputTextWithHint.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packsc(hint), rpr_packs(bufInOutNeedBig), c_int(bufInOutNeedBig_sz), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InputTextWithHint.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)
  return rval, rpr_unpacks(args[3])

@reapy.inside_reaper()
def InvisibleButton(ctx, str_id, size_w, size_h, flagsInOptional = None):
  if not hasattr(InvisibleButton, 'func'):
    proc = rpr_getfp('ImGui_InvisibleButton')
    InvisibleButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_double(size_w), c_double(size_h), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = InvisibleButton.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval

@reapy.inside_reaper()
def IsAnyItemActive(ctx):
  if not hasattr(IsAnyItemActive, 'func'):
    proc = rpr_getfp('ImGui_IsAnyItemActive')
    IsAnyItemActive.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsAnyItemActive.func(args[0])
  return rval

@reapy.inside_reaper()
def IsAnyItemFocused(ctx):
  if not hasattr(IsAnyItemFocused, 'func'):
    proc = rpr_getfp('ImGui_IsAnyItemFocused')
    IsAnyItemFocused.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsAnyItemFocused.func(args[0])
  return rval

@reapy.inside_reaper()
def IsAnyItemHovered(ctx):
  if not hasattr(IsAnyItemHovered, 'func'):
    proc = rpr_getfp('ImGui_IsAnyItemHovered')
    IsAnyItemHovered.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsAnyItemHovered.func(args[0])
  return rval

@reapy.inside_reaper()
def IsAnyMouseDown(ctx):
  if not hasattr(IsAnyMouseDown, 'func'):
    proc = rpr_getfp('ImGui_IsAnyMouseDown')
    IsAnyMouseDown.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsAnyMouseDown.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemActivated(ctx):
  if not hasattr(IsItemActivated, 'func'):
    proc = rpr_getfp('ImGui_IsItemActivated')
    IsItemActivated.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemActivated.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemActive(ctx):
  if not hasattr(IsItemActive, 'func'):
    proc = rpr_getfp('ImGui_IsItemActive')
    IsItemActive.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemActive.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemClicked(ctx, mouse_buttonInOptional = None):
  if not hasattr(IsItemClicked, 'func'):
    proc = rpr_getfp('ImGui_IsItemClicked')
    IsItemClicked.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(mouse_buttonInOptional) if mouse_buttonInOptional != None else None)
  rval = IsItemClicked.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

@reapy.inside_reaper()
def IsItemDeactivated(ctx):
  if not hasattr(IsItemDeactivated, 'func'):
    proc = rpr_getfp('ImGui_IsItemDeactivated')
    IsItemDeactivated.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemDeactivated.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemDeactivatedAfterEdit(ctx):
  if not hasattr(IsItemDeactivatedAfterEdit, 'func'):
    proc = rpr_getfp('ImGui_IsItemDeactivatedAfterEdit')
    IsItemDeactivatedAfterEdit.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemDeactivatedAfterEdit.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemEdited(ctx):
  if not hasattr(IsItemEdited, 'func'):
    proc = rpr_getfp('ImGui_IsItemEdited')
    IsItemEdited.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemEdited.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemFocused(ctx):
  if not hasattr(IsItemFocused, 'func'):
    proc = rpr_getfp('ImGui_IsItemFocused')
    IsItemFocused.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemFocused.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemHovered(ctx, flagsInOptional = None):
  if not hasattr(IsItemHovered, 'func'):
    proc = rpr_getfp('ImGui_IsItemHovered')
    IsItemHovered.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = IsItemHovered.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

@reapy.inside_reaper()
def IsItemToggledOpen(ctx):
  if not hasattr(IsItemToggledOpen, 'func'):
    proc = rpr_getfp('ImGui_IsItemToggledOpen')
    IsItemToggledOpen.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemToggledOpen.func(args[0])
  return rval

@reapy.inside_reaper()
def IsItemVisible(ctx):
  if not hasattr(IsItemVisible, 'func'):
    proc = rpr_getfp('ImGui_IsItemVisible')
    IsItemVisible.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsItemVisible.func(args[0])
  return rval

@reapy.inside_reaper()
def IsKeyDown(ctx, key_code):
  if not hasattr(IsKeyDown, 'func'):
    proc = rpr_getfp('ImGui_IsKeyDown')
    IsKeyDown.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(key_code))
  rval = IsKeyDown.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def IsKeyPressed(ctx, key_code, repeatInOptional = None):
  if not hasattr(IsKeyPressed, 'func'):
    proc = rpr_getfp('ImGui_IsKeyPressed')
    IsKeyPressed.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(key_code), c_bool(repeatInOptional) if repeatInOptional != None else None)
  rval = IsKeyPressed.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def IsKeyReleased(ctx, key_code):
  if not hasattr(IsKeyReleased, 'func'):
    proc = rpr_getfp('ImGui_IsKeyReleased')
    IsKeyReleased.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(key_code))
  rval = IsKeyReleased.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def IsMouseClicked(ctx, button, repeatInOptional = None):
  if not hasattr(IsMouseClicked, 'func'):
    proc = rpr_getfp('ImGui_IsMouseClicked')
    IsMouseClicked.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button), c_bool(repeatInOptional) if repeatInOptional != None else None)
  rval = IsMouseClicked.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def IsMouseDoubleClicked(ctx, button):
  if not hasattr(IsMouseDoubleClicked, 'func'):
    proc = rpr_getfp('ImGui_IsMouseDoubleClicked')
    IsMouseDoubleClicked.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button))
  rval = IsMouseDoubleClicked.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def IsMouseDown(ctx, button):
  if not hasattr(IsMouseDown, 'func'):
    proc = rpr_getfp('ImGui_IsMouseDown')
    IsMouseDown.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button))
  rval = IsMouseDown.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def IsMouseDragging(ctx, button, lock_thresholdInOptional = None):
  if not hasattr(IsMouseDragging, 'func'):
    proc = rpr_getfp('ImGui_IsMouseDragging')
    IsMouseDragging.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button), c_double(lock_thresholdInOptional) if lock_thresholdInOptional != None else None)
  rval = IsMouseDragging.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def IsMouseHoveringRect(ctx, r_min_x, r_min_y, r_max_x, r_max_y, clipInOptional = None):
  if not hasattr(IsMouseHoveringRect, 'func'):
    proc = rpr_getfp('ImGui_IsMouseHoveringRect')
    IsMouseHoveringRect.func = CFUNCTYPE(c_bool, c_void_p, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(r_min_x), c_double(r_min_y), c_double(r_max_x), c_double(r_max_y), c_bool(clipInOptional) if clipInOptional != None else None)
  rval = IsMouseHoveringRect.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)
  return rval

@reapy.inside_reaper()
def IsMousePosValid(ctx, mouse_pos_xInOptional = None, mouse_pos_yInOptional = None):
  if not hasattr(IsMousePosValid, 'func'):
    proc = rpr_getfp('ImGui_IsMousePosValid')
    IsMousePosValid.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(mouse_pos_xInOptional) if mouse_pos_xInOptional != None else None, c_double(mouse_pos_yInOptional) if mouse_pos_yInOptional != None else None)
  rval = IsMousePosValid.func(args[0], byref(args[1]) if args[1] != None else None, byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def IsMouseReleased(ctx, button):
  if not hasattr(IsMouseReleased, 'func'):
    proc = rpr_getfp('ImGui_IsMouseReleased')
    IsMouseReleased.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(button))
  rval = IsMouseReleased.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def IsPopupOpen(ctx, str_id, flagsInOptional = None):
  if not hasattr(IsPopupOpen, 'func'):
    proc = rpr_getfp('ImGui_IsPopupOpen')
    IsPopupOpen.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = IsPopupOpen.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def IsRectVisible(ctx, size_w, size_h):
  if not hasattr(IsRectVisible, 'func'):
    proc = rpr_getfp('ImGui_IsRectVisible')
    IsRectVisible.func = CFUNCTYPE(c_bool, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(size_w), c_double(size_h))
  rval = IsRectVisible.func(args[0], args[1], args[2])
  return rval

@reapy.inside_reaper()
def IsRectVisibleEx(ctx, rect_min_x, rect_min_y, rect_max_x, rect_max_y):
  if not hasattr(IsRectVisibleEx, 'func'):
    proc = rpr_getfp('ImGui_IsRectVisibleEx')
    IsRectVisibleEx.func = CFUNCTYPE(c_bool, c_void_p, c_double, c_double, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(rect_min_x), c_double(rect_min_y), c_double(rect_max_x), c_double(rect_max_y))
  rval = IsRectVisibleEx.func(args[0], args[1], args[2], args[3], args[4])
  return rval

@reapy.inside_reaper()
def IsWindowAppearing(ctx):
  if not hasattr(IsWindowAppearing, 'func'):
    proc = rpr_getfp('ImGui_IsWindowAppearing')
    IsWindowAppearing.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsWindowAppearing.func(args[0])
  return rval

@reapy.inside_reaper()
def IsWindowCollapsed(ctx):
  if not hasattr(IsWindowCollapsed, 'func'):
    proc = rpr_getfp('ImGui_IsWindowCollapsed')
    IsWindowCollapsed.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsWindowCollapsed.func(args[0])
  return rval

@reapy.inside_reaper()
def IsWindowDocked(ctx):
  if not hasattr(IsWindowDocked, 'func'):
    proc = rpr_getfp('ImGui_IsWindowDocked')
    IsWindowDocked.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = IsWindowDocked.func(args[0])
  return rval

@reapy.inside_reaper()
def IsWindowFocused(ctx, flagsInOptional = None):
  if not hasattr(IsWindowFocused, 'func'):
    proc = rpr_getfp('ImGui_IsWindowFocused')
    IsWindowFocused.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = IsWindowFocused.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

@reapy.inside_reaper()
def IsWindowHovered(ctx, flagsInOptional = None):
  if not hasattr(IsWindowHovered, 'func'):
    proc = rpr_getfp('ImGui_IsWindowHovered')
    IsWindowHovered.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = IsWindowHovered.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

@reapy.inside_reaper()
def KeyModFlags_Alt():
  if not hasattr(KeyModFlags_Alt, 'func'):
    proc = rpr_getfp('ImGui_KeyModFlags_Alt')
    KeyModFlags_Alt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(KeyModFlags_Alt, 'cache'):
    KeyModFlags_Alt.cache = KeyModFlags_Alt.func()
  return KeyModFlags_Alt.cache

@reapy.inside_reaper()
def KeyModFlags_Ctrl():
  if not hasattr(KeyModFlags_Ctrl, 'func'):
    proc = rpr_getfp('ImGui_KeyModFlags_Ctrl')
    KeyModFlags_Ctrl.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(KeyModFlags_Ctrl, 'cache'):
    KeyModFlags_Ctrl.cache = KeyModFlags_Ctrl.func()
  return KeyModFlags_Ctrl.cache

@reapy.inside_reaper()
def KeyModFlags_None():
  if not hasattr(KeyModFlags_None, 'func'):
    proc = rpr_getfp('ImGui_KeyModFlags_None')
    KeyModFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(KeyModFlags_None, 'cache'):
    KeyModFlags_None.cache = KeyModFlags_None.func()
  return KeyModFlags_None.cache

@reapy.inside_reaper()
def KeyModFlags_Shift():
  if not hasattr(KeyModFlags_Shift, 'func'):
    proc = rpr_getfp('ImGui_KeyModFlags_Shift')
    KeyModFlags_Shift.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(KeyModFlags_Shift, 'cache'):
    KeyModFlags_Shift.cache = KeyModFlags_Shift.func()
  return KeyModFlags_Shift.cache

@reapy.inside_reaper()
def KeyModFlags_Super():
  if not hasattr(KeyModFlags_Super, 'func'):
    proc = rpr_getfp('ImGui_KeyModFlags_Super')
    KeyModFlags_Super.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(KeyModFlags_Super, 'cache'):
    KeyModFlags_Super.cache = KeyModFlags_Super.func()
  return KeyModFlags_Super.cache

@reapy.inside_reaper()
def LabelText(ctx, label, text):
  if not hasattr(LabelText, 'func'):
    proc = rpr_getfp('ImGui_LabelText')
    LabelText.func = CFUNCTYPE(None, c_void_p, c_char_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packsc(text))
  LabelText.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def ListBox(ctx, label, current_itemInOut, items, height_in_itemsInOptional = None):
  if not hasattr(ListBox, 'func'):
    proc = rpr_getfp('ImGui_ListBox')
    ListBox.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(current_itemInOut), rpr_packs(items), c_int(height_in_itemsInOptional) if height_in_itemsInOptional != None else None)
  rval = ListBox.func(args[0], args[1], byref(args[2]), args[3], byref(args[4]) if args[4] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ListClipper_Begin(clipper, items_count, items_heightInOptional = None):
  if not hasattr(ListClipper_Begin, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_Begin')
    ListClipper_Begin.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ListClipper*', clipper), c_int(items_count), c_double(items_heightInOptional) if items_heightInOptional != None else None)
  ListClipper_Begin.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def ListClipper_End(clipper):
  if not hasattr(ListClipper_End, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_End')
    ListClipper_End.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ListClipper*', clipper),)
  ListClipper_End.func(args[0])

@reapy.inside_reaper()
def ListClipper_GetDisplayRange(clipper, display_startOut = None, display_endOut = None):
  if not hasattr(ListClipper_GetDisplayRange, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_GetDisplayRange')
    ListClipper_GetDisplayRange.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ListClipper*', clipper), c_int(display_startOut if display_startOut != None else 0), c_int(display_endOut if display_endOut != None else 0))
  ListClipper_GetDisplayRange.func(args[0], byref(args[1]), byref(args[2]))
  return int(args[1].value), int(args[2].value)

@reapy.inside_reaper()
def ListClipper_Step(clipper):
  if not hasattr(ListClipper_Step, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_Step')
    ListClipper_Step.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ListClipper*', clipper),)
  rval = ListClipper_Step.func(args[0])
  return rval

@reapy.inside_reaper()
def LogFinish(ctx):
  if not hasattr(LogFinish, 'func'):
    proc = rpr_getfp('ImGui_LogFinish')
    LogFinish.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  LogFinish.func(args[0])

@reapy.inside_reaper()
def LogText(ctx, text):
  if not hasattr(LogText, 'func'):
    proc = rpr_getfp('ImGui_LogText')
    LogText.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  LogText.func(args[0], args[1])

@reapy.inside_reaper()
def LogToClipboard(ctx, auto_open_depthInOptional = None):
  if not hasattr(LogToClipboard, 'func'):
    proc = rpr_getfp('ImGui_LogToClipboard')
    LogToClipboard.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(auto_open_depthInOptional) if auto_open_depthInOptional != None else None)
  LogToClipboard.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def LogToFile(ctx, auto_open_depthInOptional = None, filenameInOptional = None):
  if not hasattr(LogToFile, 'func'):
    proc = rpr_getfp('ImGui_LogToFile')
    LogToFile.func = CFUNCTYPE(None, c_void_p, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(auto_open_depthInOptional) if auto_open_depthInOptional != None else None, rpr_packsc(filenameInOptional) if filenameInOptional != None else None)
  LogToFile.func(args[0], byref(args[1]) if args[1] != None else None, args[2])

@reapy.inside_reaper()
def LogToTTY(ctx, auto_open_depthInOptional = None):
  if not hasattr(LogToTTY, 'func'):
    proc = rpr_getfp('ImGui_LogToTTY')
    LogToTTY.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(auto_open_depthInOptional) if auto_open_depthInOptional != None else None)
  LogToTTY.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def MenuItem(ctx, label, shortcutInOptional = None, p_selectedInOutOptional = None, enabledInOptional = None):
  if not hasattr(MenuItem, 'func'):
    proc = rpr_getfp('ImGui_MenuItem')
    MenuItem.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packsc(shortcutInOptional) if shortcutInOptional != None else None, c_bool(p_selectedInOutOptional) if p_selectedInOutOptional != None else None, c_bool(enabledInOptional) if enabledInOptional != None else None)
  rval = MenuItem.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)
  return rval, int(args[3].value) if p_selectedInOutOptional != None else None

@reapy.inside_reaper()
def MouseButton_Left():
  if not hasattr(MouseButton_Left, 'func'):
    proc = rpr_getfp('ImGui_MouseButton_Left')
    MouseButton_Left.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseButton_Left, 'cache'):
    MouseButton_Left.cache = MouseButton_Left.func()
  return MouseButton_Left.cache

@reapy.inside_reaper()
def MouseButton_Middle():
  if not hasattr(MouseButton_Middle, 'func'):
    proc = rpr_getfp('ImGui_MouseButton_Middle')
    MouseButton_Middle.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseButton_Middle, 'cache'):
    MouseButton_Middle.cache = MouseButton_Middle.func()
  return MouseButton_Middle.cache

@reapy.inside_reaper()
def MouseButton_Right():
  if not hasattr(MouseButton_Right, 'func'):
    proc = rpr_getfp('ImGui_MouseButton_Right')
    MouseButton_Right.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseButton_Right, 'cache'):
    MouseButton_Right.cache = MouseButton_Right.func()
  return MouseButton_Right.cache

@reapy.inside_reaper()
def MouseCursor_Arrow():
  if not hasattr(MouseCursor_Arrow, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_Arrow')
    MouseCursor_Arrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_Arrow, 'cache'):
    MouseCursor_Arrow.cache = MouseCursor_Arrow.func()
  return MouseCursor_Arrow.cache

@reapy.inside_reaper()
def MouseCursor_Hand():
  if not hasattr(MouseCursor_Hand, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_Hand')
    MouseCursor_Hand.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_Hand, 'cache'):
    MouseCursor_Hand.cache = MouseCursor_Hand.func()
  return MouseCursor_Hand.cache

@reapy.inside_reaper()
def MouseCursor_NotAllowed():
  if not hasattr(MouseCursor_NotAllowed, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_NotAllowed')
    MouseCursor_NotAllowed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_NotAllowed, 'cache'):
    MouseCursor_NotAllowed.cache = MouseCursor_NotAllowed.func()
  return MouseCursor_NotAllowed.cache

@reapy.inside_reaper()
def MouseCursor_ResizeAll():
  if not hasattr(MouseCursor_ResizeAll, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeAll')
    MouseCursor_ResizeAll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_ResizeAll, 'cache'):
    MouseCursor_ResizeAll.cache = MouseCursor_ResizeAll.func()
  return MouseCursor_ResizeAll.cache

@reapy.inside_reaper()
def MouseCursor_ResizeEW():
  if not hasattr(MouseCursor_ResizeEW, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeEW')
    MouseCursor_ResizeEW.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_ResizeEW, 'cache'):
    MouseCursor_ResizeEW.cache = MouseCursor_ResizeEW.func()
  return MouseCursor_ResizeEW.cache

@reapy.inside_reaper()
def MouseCursor_ResizeNESW():
  if not hasattr(MouseCursor_ResizeNESW, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeNESW')
    MouseCursor_ResizeNESW.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_ResizeNESW, 'cache'):
    MouseCursor_ResizeNESW.cache = MouseCursor_ResizeNESW.func()
  return MouseCursor_ResizeNESW.cache

@reapy.inside_reaper()
def MouseCursor_ResizeNS():
  if not hasattr(MouseCursor_ResizeNS, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeNS')
    MouseCursor_ResizeNS.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_ResizeNS, 'cache'):
    MouseCursor_ResizeNS.cache = MouseCursor_ResizeNS.func()
  return MouseCursor_ResizeNS.cache

@reapy.inside_reaper()
def MouseCursor_ResizeNWSE():
  if not hasattr(MouseCursor_ResizeNWSE, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeNWSE')
    MouseCursor_ResizeNWSE.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_ResizeNWSE, 'cache'):
    MouseCursor_ResizeNWSE.cache = MouseCursor_ResizeNWSE.func()
  return MouseCursor_ResizeNWSE.cache

@reapy.inside_reaper()
def MouseCursor_TextInput():
  if not hasattr(MouseCursor_TextInput, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_TextInput')
    MouseCursor_TextInput.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(MouseCursor_TextInput, 'cache'):
    MouseCursor_TextInput.cache = MouseCursor_TextInput.func()
  return MouseCursor_TextInput.cache

@reapy.inside_reaper()
def NewLine(ctx):
  if not hasattr(NewLine, 'func'):
    proc = rpr_getfp('ImGui_NewLine')
    NewLine.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  NewLine.func(args[0])

@reapy.inside_reaper()
def NumericLimits_Float(minOut = None, maxOut = None):
  if not hasattr(NumericLimits_Float, 'func'):
    proc = rpr_getfp('ImGui_NumericLimits_Float')
    NumericLimits_Float.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (c_double(minOut if minOut != None else 0), c_double(maxOut if maxOut != None else 0))
  NumericLimits_Float.func(byref(args[0]), byref(args[1]))
  return float(args[0].value), float(args[1].value)

@reapy.inside_reaper()
def OpenPopup(ctx, str_id, popup_flagsInOptional = None):
  if not hasattr(OpenPopup, 'func'):
    proc = rpr_getfp('ImGui_OpenPopup')
    OpenPopup.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  OpenPopup.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def OpenPopupOnItemClick(ctx, str_idInOptional = None, popup_flagsInOptional = None):
  if not hasattr(OpenPopupOnItemClick, 'func'):
    proc = rpr_getfp('ImGui_OpenPopupOnItemClick')
    OpenPopupOnItemClick.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_idInOptional) if str_idInOptional != None else None, c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  OpenPopupOnItemClick.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def PlotHistogram(ctx, label, values, values_offsetInOptional = None, overlay_textInOptional = None, scale_minInOptional = None, scale_maxInOptional = None, graph_size_wInOptional = None, graph_size_hInOptional = None):
  if not hasattr(PlotHistogram, 'func'):
    proc = rpr_getfp('ImGui_PlotHistogram')
    PlotHistogram.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_int(values_offsetInOptional) if values_offsetInOptional != None else None, rpr_packsc(overlay_textInOptional) if overlay_textInOptional != None else None, c_double(scale_minInOptional) if scale_minInOptional != None else None, c_double(scale_maxInOptional) if scale_maxInOptional != None else None, c_double(graph_size_wInOptional) if graph_size_wInOptional != None else None, c_double(graph_size_hInOptional) if graph_size_hInOptional != None else None)
  PlotHistogram.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None)

@reapy.inside_reaper()
def PlotLines(ctx, label, values, values_offsetInOptional = None, overlay_textInOptional = None, scale_minInOptional = None, scale_maxInOptional = None, graph_size_wInOptional = None, graph_size_hInOptional = None):
  if not hasattr(PlotLines, 'func'):
    proc = rpr_getfp('ImGui_PlotLines')
    PlotLines.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_int(values_offsetInOptional) if values_offsetInOptional != None else None, rpr_packsc(overlay_textInOptional) if overlay_textInOptional != None else None, c_double(scale_minInOptional) if scale_minInOptional != None else None, c_double(scale_maxInOptional) if scale_maxInOptional != None else None, c_double(graph_size_wInOptional) if graph_size_wInOptional != None else None, c_double(graph_size_hInOptional) if graph_size_hInOptional != None else None)
  PlotLines.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None)

@reapy.inside_reaper()
def PointConvertNative(ctx, xInOut, yInOut, to_nativeInOptional = None):
  if not hasattr(PointConvertNative, 'func'):
    proc = rpr_getfp('ImGui_PointConvertNative')
    PointConvertNative.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(xInOut), c_double(yInOut), c_bool(to_nativeInOptional) if to_nativeInOptional != None else None)
  PointConvertNative.func(args[0], byref(args[1]), byref(args[2]), byref(args[3]) if args[3] != None else None)
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def PopAllowKeyboardFocus(ctx):
  if not hasattr(PopAllowKeyboardFocus, 'func'):
    proc = rpr_getfp('ImGui_PopAllowKeyboardFocus')
    PopAllowKeyboardFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopAllowKeyboardFocus.func(args[0])

@reapy.inside_reaper()
def PopButtonRepeat(ctx):
  if not hasattr(PopButtonRepeat, 'func'):
    proc = rpr_getfp('ImGui_PopButtonRepeat')
    PopButtonRepeat.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopButtonRepeat.func(args[0])

@reapy.inside_reaper()
def PopClipRect(ctx):
  if not hasattr(PopClipRect, 'func'):
    proc = rpr_getfp('ImGui_PopClipRect')
    PopClipRect.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopClipRect.func(args[0])

@reapy.inside_reaper()
def PopFont(ctx):
  if not hasattr(PopFont, 'func'):
    proc = rpr_getfp('ImGui_PopFont')
    PopFont.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopFont.func(args[0])

@reapy.inside_reaper()
def PopID(ctx):
  if not hasattr(PopID, 'func'):
    proc = rpr_getfp('ImGui_PopID')
    PopID.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopID.func(args[0])

@reapy.inside_reaper()
def PopItemWidth(ctx):
  if not hasattr(PopItemWidth, 'func'):
    proc = rpr_getfp('ImGui_PopItemWidth')
    PopItemWidth.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopItemWidth.func(args[0])

@reapy.inside_reaper()
def PopStyleColor(ctx, countInOptional = None):
  if not hasattr(PopStyleColor, 'func'):
    proc = rpr_getfp('ImGui_PopStyleColor')
    PopStyleColor.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(countInOptional) if countInOptional != None else None)
  PopStyleColor.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def PopStyleVar(ctx, countInOptional = None):
  if not hasattr(PopStyleVar, 'func'):
    proc = rpr_getfp('ImGui_PopStyleVar')
    PopStyleVar.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(countInOptional) if countInOptional != None else None)
  PopStyleVar.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def PopTextWrapPos(ctx):
  if not hasattr(PopTextWrapPos, 'func'):
    proc = rpr_getfp('ImGui_PopTextWrapPos')
    PopTextWrapPos.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  PopTextWrapPos.func(args[0])

@reapy.inside_reaper()
def PopupFlags_AnyPopup():
  if not hasattr(PopupFlags_AnyPopup, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_AnyPopup')
    PopupFlags_AnyPopup.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_AnyPopup, 'cache'):
    PopupFlags_AnyPopup.cache = PopupFlags_AnyPopup.func()
  return PopupFlags_AnyPopup.cache

@reapy.inside_reaper()
def PopupFlags_AnyPopupId():
  if not hasattr(PopupFlags_AnyPopupId, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_AnyPopupId')
    PopupFlags_AnyPopupId.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_AnyPopupId, 'cache'):
    PopupFlags_AnyPopupId.cache = PopupFlags_AnyPopupId.func()
  return PopupFlags_AnyPopupId.cache

@reapy.inside_reaper()
def PopupFlags_AnyPopupLevel():
  if not hasattr(PopupFlags_AnyPopupLevel, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_AnyPopupLevel')
    PopupFlags_AnyPopupLevel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_AnyPopupLevel, 'cache'):
    PopupFlags_AnyPopupLevel.cache = PopupFlags_AnyPopupLevel.func()
  return PopupFlags_AnyPopupLevel.cache

@reapy.inside_reaper()
def PopupFlags_MouseButtonLeft():
  if not hasattr(PopupFlags_MouseButtonLeft, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_MouseButtonLeft')
    PopupFlags_MouseButtonLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_MouseButtonLeft, 'cache'):
    PopupFlags_MouseButtonLeft.cache = PopupFlags_MouseButtonLeft.func()
  return PopupFlags_MouseButtonLeft.cache

@reapy.inside_reaper()
def PopupFlags_MouseButtonMiddle():
  if not hasattr(PopupFlags_MouseButtonMiddle, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_MouseButtonMiddle')
    PopupFlags_MouseButtonMiddle.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_MouseButtonMiddle, 'cache'):
    PopupFlags_MouseButtonMiddle.cache = PopupFlags_MouseButtonMiddle.func()
  return PopupFlags_MouseButtonMiddle.cache

@reapy.inside_reaper()
def PopupFlags_MouseButtonRight():
  if not hasattr(PopupFlags_MouseButtonRight, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_MouseButtonRight')
    PopupFlags_MouseButtonRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_MouseButtonRight, 'cache'):
    PopupFlags_MouseButtonRight.cache = PopupFlags_MouseButtonRight.func()
  return PopupFlags_MouseButtonRight.cache

@reapy.inside_reaper()
def PopupFlags_NoOpenOverExistingPopup():
  if not hasattr(PopupFlags_NoOpenOverExistingPopup, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_NoOpenOverExistingPopup')
    PopupFlags_NoOpenOverExistingPopup.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_NoOpenOverExistingPopup, 'cache'):
    PopupFlags_NoOpenOverExistingPopup.cache = PopupFlags_NoOpenOverExistingPopup.func()
  return PopupFlags_NoOpenOverExistingPopup.cache

@reapy.inside_reaper()
def PopupFlags_NoOpenOverItems():
  if not hasattr(PopupFlags_NoOpenOverItems, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_NoOpenOverItems')
    PopupFlags_NoOpenOverItems.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_NoOpenOverItems, 'cache'):
    PopupFlags_NoOpenOverItems.cache = PopupFlags_NoOpenOverItems.func()
  return PopupFlags_NoOpenOverItems.cache

@reapy.inside_reaper()
def PopupFlags_None():
  if not hasattr(PopupFlags_None, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_None')
    PopupFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(PopupFlags_None, 'cache'):
    PopupFlags_None.cache = PopupFlags_None.func()
  return PopupFlags_None.cache

@reapy.inside_reaper()
def ProgressBar(ctx, fraction, size_arg_wInOptional = None, size_arg_hInOptional = None, overlayInOptional = None):
  if not hasattr(ProgressBar, 'func'):
    proc = rpr_getfp('ImGui_ProgressBar')
    ProgressBar.func = CFUNCTYPE(None, c_void_p, c_double, c_void_p, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(fraction), c_double(size_arg_wInOptional) if size_arg_wInOptional != None else None, c_double(size_arg_hInOptional) if size_arg_hInOptional != None else None, rpr_packsc(overlayInOptional) if overlayInOptional != None else None)
  ProgressBar.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None, args[4])

@reapy.inside_reaper()
def PushAllowKeyboardFocus(ctx, allow_keyboard_focus):
  if not hasattr(PushAllowKeyboardFocus, 'func'):
    proc = rpr_getfp('ImGui_PushAllowKeyboardFocus')
    PushAllowKeyboardFocus.func = CFUNCTYPE(None, c_void_p, c_bool)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(allow_keyboard_focus))
  PushAllowKeyboardFocus.func(args[0], args[1])

@reapy.inside_reaper()
def PushButtonRepeat(ctx, repeat):
  if not hasattr(PushButtonRepeat, 'func'):
    proc = rpr_getfp('ImGui_PushButtonRepeat')
    PushButtonRepeat.func = CFUNCTYPE(None, c_void_p, c_bool)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(repeat))
  PushButtonRepeat.func(args[0], args[1])

@reapy.inside_reaper()
def PushClipRect(ctx, clip_rect_min_x, clip_rect_min_y, clip_rect_max_x, clip_rect_max_y, intersect_with_current_clip_rect):
  if not hasattr(PushClipRect, 'func'):
    proc = rpr_getfp('ImGui_PushClipRect')
    PushClipRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_bool)(proc)
  args = (rpr_packp('Context*', ctx), c_double(clip_rect_min_x), c_double(clip_rect_min_y), c_double(clip_rect_max_x), c_double(clip_rect_max_y), c_bool(intersect_with_current_clip_rect))
  PushClipRect.func(args[0], args[1], args[2], args[3], args[4], args[5])

@reapy.inside_reaper()
def PushFont(ctx, font):
  if not hasattr(PushFont, 'func'):
    proc = rpr_getfp('ImGui_PushFont')
    PushFont.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packp('Font*', font))
  PushFont.func(args[0], args[1])

@reapy.inside_reaper()
def PushID(ctx, str_id):
  if not hasattr(PushID, 'func'):
    proc = rpr_getfp('ImGui_PushID')
    PushID.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id))
  PushID.func(args[0], args[1])

@reapy.inside_reaper()
def PushItemWidth(ctx, item_width):
  if not hasattr(PushItemWidth, 'func'):
    proc = rpr_getfp('ImGui_PushItemWidth')
    PushItemWidth.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(item_width))
  PushItemWidth.func(args[0], args[1])

@reapy.inside_reaper()
def PushStyleColor(ctx, idx, col_rgba):
  if not hasattr(PushStyleColor, 'func'):
    proc = rpr_getfp('ImGui_PushStyleColor')
    PushStyleColor.func = CFUNCTYPE(None, c_void_p, c_int, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(idx), c_int(col_rgba))
  PushStyleColor.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def PushStyleVar(ctx, var_idx, val1, val2InOptional = None):
  if not hasattr(PushStyleVar, 'func'):
    proc = rpr_getfp('ImGui_PushStyleVar')
    PushStyleVar.func = CFUNCTYPE(None, c_void_p, c_int, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(var_idx), c_double(val1), c_double(val2InOptional) if val2InOptional != None else None)
  PushStyleVar.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def PushTextWrapPos(ctx, wrap_local_pos_xInOptional = None):
  if not hasattr(PushTextWrapPos, 'func'):
    proc = rpr_getfp('ImGui_PushTextWrapPos')
    PushTextWrapPos.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(wrap_local_pos_xInOptional) if wrap_local_pos_xInOptional != None else None)
  PushTextWrapPos.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def RadioButton(ctx, label, active):
  if not hasattr(RadioButton, 'func'):
    proc = rpr_getfp('ImGui_RadioButton')
    RadioButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_bool)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_bool(active))
  rval = RadioButton.func(args[0], args[1], args[2])
  return rval

@reapy.inside_reaper()
def RadioButtonEx(ctx, label, vInOut, v_button):
  if not hasattr(RadioButtonEx, 'func'):
    proc = rpr_getfp('ImGui_RadioButtonEx')
    RadioButtonEx.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(vInOut), c_int(v_button))
  rval = RadioButtonEx.func(args[0], args[1], byref(args[2]), args[3])
  return rval, int(args[2].value)

@reapy.inside_reaper()
def ResetMouseDragDelta(ctx, buttonInOptional = None):
  if not hasattr(ResetMouseDragDelta, 'func'):
    proc = rpr_getfp('ImGui_ResetMouseDragDelta')
    ResetMouseDragDelta.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(buttonInOptional) if buttonInOptional != None else None)
  ResetMouseDragDelta.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def SameLine(ctx, offset_from_start_xInOptional = None, spacingInOptional = None):
  if not hasattr(SameLine, 'func'):
    proc = rpr_getfp('ImGui_SameLine')
    SameLine.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(offset_from_start_xInOptional) if offset_from_start_xInOptional != None else None, c_double(spacingInOptional) if spacingInOptional != None else None)
  SameLine.func(args[0], byref(args[1]) if args[1] != None else None, byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def Selectable(ctx, label, p_selectedInOut, flagsInOptional = None, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(Selectable, 'func'):
    proc = rpr_getfp('ImGui_Selectable')
    Selectable.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_bool(p_selectedInOut), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = Selectable.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def SelectableFlags_AllowDoubleClick():
  if not hasattr(SelectableFlags_AllowDoubleClick, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_AllowDoubleClick')
    SelectableFlags_AllowDoubleClick.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SelectableFlags_AllowDoubleClick, 'cache'):
    SelectableFlags_AllowDoubleClick.cache = SelectableFlags_AllowDoubleClick.func()
  return SelectableFlags_AllowDoubleClick.cache

@reapy.inside_reaper()
def SelectableFlags_AllowItemOverlap():
  if not hasattr(SelectableFlags_AllowItemOverlap, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_AllowItemOverlap')
    SelectableFlags_AllowItemOverlap.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SelectableFlags_AllowItemOverlap, 'cache'):
    SelectableFlags_AllowItemOverlap.cache = SelectableFlags_AllowItemOverlap.func()
  return SelectableFlags_AllowItemOverlap.cache

@reapy.inside_reaper()
def SelectableFlags_Disabled():
  if not hasattr(SelectableFlags_Disabled, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_Disabled')
    SelectableFlags_Disabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SelectableFlags_Disabled, 'cache'):
    SelectableFlags_Disabled.cache = SelectableFlags_Disabled.func()
  return SelectableFlags_Disabled.cache

@reapy.inside_reaper()
def SelectableFlags_DontClosePopups():
  if not hasattr(SelectableFlags_DontClosePopups, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_DontClosePopups')
    SelectableFlags_DontClosePopups.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SelectableFlags_DontClosePopups, 'cache'):
    SelectableFlags_DontClosePopups.cache = SelectableFlags_DontClosePopups.func()
  return SelectableFlags_DontClosePopups.cache

@reapy.inside_reaper()
def SelectableFlags_None():
  if not hasattr(SelectableFlags_None, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_None')
    SelectableFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SelectableFlags_None, 'cache'):
    SelectableFlags_None.cache = SelectableFlags_None.func()
  return SelectableFlags_None.cache

@reapy.inside_reaper()
def SelectableFlags_SpanAllColumns():
  if not hasattr(SelectableFlags_SpanAllColumns, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_SpanAllColumns')
    SelectableFlags_SpanAllColumns.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SelectableFlags_SpanAllColumns, 'cache'):
    SelectableFlags_SpanAllColumns.cache = SelectableFlags_SpanAllColumns.func()
  return SelectableFlags_SpanAllColumns.cache

@reapy.inside_reaper()
def Separator(ctx):
  if not hasattr(Separator, 'func'):
    proc = rpr_getfp('ImGui_Separator')
    Separator.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  Separator.func(args[0])

@reapy.inside_reaper()
def SetClipboardText(ctx, text):
  if not hasattr(SetClipboardText, 'func'):
    proc = rpr_getfp('ImGui_SetClipboardText')
    SetClipboardText.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  SetClipboardText.func(args[0], args[1])

@reapy.inside_reaper()
def SetColorEditOptions(ctx, flags):
  if not hasattr(SetColorEditOptions, 'func'):
    proc = rpr_getfp('ImGui_SetColorEditOptions')
    SetColorEditOptions.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(flags))
  SetColorEditOptions.func(args[0], args[1])

@reapy.inside_reaper()
def SetConfigFlags(ctx, flags):
  if not hasattr(SetConfigFlags, 'func'):
    proc = rpr_getfp('ImGui_SetConfigFlags')
    SetConfigFlags.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(flags))
  SetConfigFlags.func(args[0], args[1])

@reapy.inside_reaper()
def SetCursorPos(ctx, local_pos_x, local_pos_y):
  if not hasattr(SetCursorPos, 'func'):
    proc = rpr_getfp('ImGui_SetCursorPos')
    SetCursorPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(local_pos_x), c_double(local_pos_y))
  SetCursorPos.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def SetCursorPosX(ctx, local_x):
  if not hasattr(SetCursorPosX, 'func'):
    proc = rpr_getfp('ImGui_SetCursorPosX')
    SetCursorPosX.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(local_x))
  SetCursorPosX.func(args[0], args[1])

@reapy.inside_reaper()
def SetCursorPosY(ctx, local_y):
  if not hasattr(SetCursorPosY, 'func'):
    proc = rpr_getfp('ImGui_SetCursorPosY')
    SetCursorPosY.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(local_y))
  SetCursorPosY.func(args[0], args[1])

@reapy.inside_reaper()
def SetCursorScreenPos(ctx, pos_x, pos_y):
  if not hasattr(SetCursorScreenPos, 'func'):
    proc = rpr_getfp('ImGui_SetCursorScreenPos')
    SetCursorScreenPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(pos_x), c_double(pos_y))
  SetCursorScreenPos.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def SetDragDropPayload(ctx, type, data, condInOptional = None):
  if not hasattr(SetDragDropPayload, 'func'):
    proc = rpr_getfp('ImGui_SetDragDropPayload')
    SetDragDropPayload.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(type), rpr_packsc(data), c_int(condInOptional) if condInOptional != None else None)
  rval = SetDragDropPayload.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

@reapy.inside_reaper()
def SetItemAllowOverlap(ctx):
  if not hasattr(SetItemAllowOverlap, 'func'):
    proc = rpr_getfp('ImGui_SetItemAllowOverlap')
    SetItemAllowOverlap.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  SetItemAllowOverlap.func(args[0])

@reapy.inside_reaper()
def SetItemDefaultFocus(ctx):
  if not hasattr(SetItemDefaultFocus, 'func'):
    proc = rpr_getfp('ImGui_SetItemDefaultFocus')
    SetItemDefaultFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  SetItemDefaultFocus.func(args[0])

@reapy.inside_reaper()
def SetKeyboardFocusHere(ctx, offsetInOptional = None):
  if not hasattr(SetKeyboardFocusHere, 'func'):
    proc = rpr_getfp('ImGui_SetKeyboardFocusHere')
    SetKeyboardFocusHere.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(offsetInOptional) if offsetInOptional != None else None)
  SetKeyboardFocusHere.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def SetMouseCursor(ctx, cursor_type):
  if not hasattr(SetMouseCursor, 'func'):
    proc = rpr_getfp('ImGui_SetMouseCursor')
    SetMouseCursor.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(cursor_type))
  SetMouseCursor.func(args[0], args[1])

@reapy.inside_reaper()
def SetNextItemOpen(ctx, is_open, condInOptional = None):
  if not hasattr(SetNextItemOpen, 'func'):
    proc = rpr_getfp('ImGui_SetNextItemOpen')
    SetNextItemOpen.func = CFUNCTYPE(None, c_void_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(is_open), c_int(condInOptional) if condInOptional != None else None)
  SetNextItemOpen.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def SetNextItemWidth(ctx, item_width):
  if not hasattr(SetNextItemWidth, 'func'):
    proc = rpr_getfp('ImGui_SetNextItemWidth')
    SetNextItemWidth.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(item_width))
  SetNextItemWidth.func(args[0], args[1])

@reapy.inside_reaper()
def SetNextWindowBgAlpha(ctx, alpha):
  if not hasattr(SetNextWindowBgAlpha, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowBgAlpha')
    SetNextWindowBgAlpha.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(alpha))
  SetNextWindowBgAlpha.func(args[0], args[1])

@reapy.inside_reaper()
def SetNextWindowCollapsed(ctx, collapsed, condInOptional = None):
  if not hasattr(SetNextWindowCollapsed, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowCollapsed')
    SetNextWindowCollapsed.func = CFUNCTYPE(None, c_void_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(collapsed), c_int(condInOptional) if condInOptional != None else None)
  SetNextWindowCollapsed.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def SetNextWindowContentSize(ctx, size_w, size_h):
  if not hasattr(SetNextWindowContentSize, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowContentSize')
    SetNextWindowContentSize.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(size_w), c_double(size_h))
  SetNextWindowContentSize.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def SetNextWindowDockID(ctx, dock_id, condInOptional = None):
  if not hasattr(SetNextWindowDockID, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowDockID')
    SetNextWindowDockID.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(dock_id), c_int(condInOptional) if condInOptional != None else None)
  SetNextWindowDockID.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def SetNextWindowFocus(ctx):
  if not hasattr(SetNextWindowFocus, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowFocus')
    SetNextWindowFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  SetNextWindowFocus.func(args[0])

@reapy.inside_reaper()
def SetNextWindowPos(ctx, pos_x, pos_y, condInOptional = None, pivot_xInOptional = None, pivot_yInOptional = None):
  if not hasattr(SetNextWindowPos, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowPos')
    SetNextWindowPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(pos_x), c_double(pos_y), c_int(condInOptional) if condInOptional != None else None, c_double(pivot_xInOptional) if pivot_xInOptional != None else None, c_double(pivot_yInOptional) if pivot_yInOptional != None else None)
  SetNextWindowPos.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)

@reapy.inside_reaper()
def SetNextWindowSize(ctx, size_w, size_h, condInOptional = None):
  if not hasattr(SetNextWindowSize, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowSize')
    SetNextWindowSize.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(size_w), c_double(size_h), c_int(condInOptional) if condInOptional != None else None)
  SetNextWindowSize.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def SetNextWindowSizeConstraints(ctx, size_min_w, size_min_h, size_max_w, size_max_h):
  if not hasattr(SetNextWindowSizeConstraints, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowSizeConstraints')
    SetNextWindowSizeConstraints.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(size_min_w), c_double(size_min_h), c_double(size_max_w), c_double(size_max_h))
  SetNextWindowSizeConstraints.func(args[0], args[1], args[2], args[3], args[4])

@reapy.inside_reaper()
def SetScrollFromPosX(ctx, local_x, center_x_ratioInOptional = None):
  if not hasattr(SetScrollFromPosX, 'func'):
    proc = rpr_getfp('ImGui_SetScrollFromPosX')
    SetScrollFromPosX.func = CFUNCTYPE(None, c_void_p, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(local_x), c_double(center_x_ratioInOptional) if center_x_ratioInOptional != None else None)
  SetScrollFromPosX.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def SetScrollFromPosY(ctx, local_y, center_y_ratioInOptional = None):
  if not hasattr(SetScrollFromPosY, 'func'):
    proc = rpr_getfp('ImGui_SetScrollFromPosY')
    SetScrollFromPosY.func = CFUNCTYPE(None, c_void_p, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(local_y), c_double(center_y_ratioInOptional) if center_y_ratioInOptional != None else None)
  SetScrollFromPosY.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def SetScrollHereX(ctx, center_x_ratioInOptional = None):
  if not hasattr(SetScrollHereX, 'func'):
    proc = rpr_getfp('ImGui_SetScrollHereX')
    SetScrollHereX.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(center_x_ratioInOptional) if center_x_ratioInOptional != None else None)
  SetScrollHereX.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def SetScrollHereY(ctx, center_y_ratioInOptional = None):
  if not hasattr(SetScrollHereY, 'func'):
    proc = rpr_getfp('ImGui_SetScrollHereY')
    SetScrollHereY.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(center_y_ratioInOptional) if center_y_ratioInOptional != None else None)
  SetScrollHereY.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def SetScrollX(ctx, scroll_x):
  if not hasattr(SetScrollX, 'func'):
    proc = rpr_getfp('ImGui_SetScrollX')
    SetScrollX.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(scroll_x))
  SetScrollX.func(args[0], args[1])

@reapy.inside_reaper()
def SetScrollY(ctx, scroll_y):
  if not hasattr(SetScrollY, 'func'):
    proc = rpr_getfp('ImGui_SetScrollY')
    SetScrollY.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('Context*', ctx), c_double(scroll_y))
  SetScrollY.func(args[0], args[1])

@reapy.inside_reaper()
def SetTabItemClosed(ctx, tab_or_docked_window_label):
  if not hasattr(SetTabItemClosed, 'func'):
    proc = rpr_getfp('ImGui_SetTabItemClosed')
    SetTabItemClosed.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(tab_or_docked_window_label))
  SetTabItemClosed.func(args[0], args[1])

@reapy.inside_reaper()
def SetTooltip(ctx, text):
  if not hasattr(SetTooltip, 'func'):
    proc = rpr_getfp('ImGui_SetTooltip')
    SetTooltip.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  SetTooltip.func(args[0], args[1])

@reapy.inside_reaper()
def SetWindowCollapsed(ctx, collapsed, condInOptional = None):
  if not hasattr(SetWindowCollapsed, 'func'):
    proc = rpr_getfp('ImGui_SetWindowCollapsed')
    SetWindowCollapsed.func = CFUNCTYPE(None, c_void_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(collapsed), c_int(condInOptional) if condInOptional != None else None)
  SetWindowCollapsed.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def SetWindowCollapsedEx(ctx, name, collapsed, condInOptional = None):
  if not hasattr(SetWindowCollapsedEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowCollapsedEx')
    SetWindowCollapsedEx.func = CFUNCTYPE(None, c_void_p, c_char_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(name), c_bool(collapsed), c_int(condInOptional) if condInOptional != None else None)
  SetWindowCollapsedEx.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def SetWindowFocus(ctx):
  if not hasattr(SetWindowFocus, 'func'):
    proc = rpr_getfp('ImGui_SetWindowFocus')
    SetWindowFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  SetWindowFocus.func(args[0])

@reapy.inside_reaper()
def SetWindowFocusEx(ctx, name):
  if not hasattr(SetWindowFocusEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowFocusEx')
    SetWindowFocusEx.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(name))
  SetWindowFocusEx.func(args[0], args[1])

@reapy.inside_reaper()
def SetWindowPos(ctx, pos_x, pos_y, condInOptional = None):
  if not hasattr(SetWindowPos, 'func'):
    proc = rpr_getfp('ImGui_SetWindowPos')
    SetWindowPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(pos_x), c_double(pos_y), c_int(condInOptional) if condInOptional != None else None)
  SetWindowPos.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def SetWindowPosEx(ctx, name, pos_x, pos_y, condInOptional = None):
  if not hasattr(SetWindowPosEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowPosEx')
    SetWindowPosEx.func = CFUNCTYPE(None, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(name), c_double(pos_x), c_double(pos_y), c_int(condInOptional) if condInOptional != None else None)
  SetWindowPosEx.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)

@reapy.inside_reaper()
def SetWindowSize(ctx, size_w, size_h, condInOptional = None):
  if not hasattr(SetWindowSize, 'func'):
    proc = rpr_getfp('ImGui_SetWindowSize')
    SetWindowSize.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(size_w), c_double(size_h), c_int(condInOptional) if condInOptional != None else None)
  SetWindowSize.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def SetWindowSizeEx(ctx, name, size_w, size_h, condInOptional = None):
  if not hasattr(SetWindowSizeEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowSizeEx')
    SetWindowSizeEx.func = CFUNCTYPE(None, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(name), c_double(size_w), c_double(size_h), c_int(condInOptional) if condInOptional != None else None)
  SetWindowSizeEx.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)

@reapy.inside_reaper()
def ShowAboutWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ShowAboutWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowAboutWindow')
    ShowAboutWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ShowAboutWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

@reapy.inside_reaper()
def ShowMetricsWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ShowMetricsWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowMetricsWindow')
    ShowMetricsWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ShowMetricsWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

@reapy.inside_reaper()
def ShowStackToolWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ShowStackToolWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowStackToolWindow')
    ShowStackToolWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ShowStackToolWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

@reapy.inside_reaper()
def SliderAngle(ctx, label, v_radInOut, v_degrees_minInOptional = None, v_degrees_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderAngle, 'func'):
    proc = rpr_getfp('ImGui_SliderAngle')
    SliderAngle.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v_radInOut), c_double(v_degrees_minInOptional) if v_degrees_minInOptional != None else None, c_double(v_degrees_maxInOptional) if v_degrees_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderAngle.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value)

@reapy.inside_reaper()
def SliderDouble(ctx, label, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderDouble, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble')
    SliderDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(vInOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderDouble.func(args[0], args[1], byref(args[2]), args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value)

@reapy.inside_reaper()
def SliderDouble2(ctx, label, v1InOut, v2InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderDouble2, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble2')
    SliderDouble2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderDouble2.func(args[0], args[1], byref(args[2]), byref(args[3]), args[4], args[5], args[6], byref(args[7]) if args[7] != None else None)
  return rval, float(args[2].value), float(args[3].value)

@reapy.inside_reaper()
def SliderDouble3(ctx, label, v1InOut, v2InOut, v3InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderDouble3, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble3')
    SliderDouble3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderDouble3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value)

@reapy.inside_reaper()
def SliderDouble4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderDouble4, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble4')
    SliderDouble4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v4InOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderDouble4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), args[6], args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value), float(args[5].value)

@reapy.inside_reaper()
def SliderDoubleN(ctx, label, values, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderDoubleN, 'func'):
    proc = rpr_getfp('ImGui_SliderDoubleN')
    SliderDoubleN.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderDoubleN.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)
  return rval

@reapy.inside_reaper()
def SliderFlags_AlwaysClamp():
  if not hasattr(SliderFlags_AlwaysClamp, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_AlwaysClamp')
    SliderFlags_AlwaysClamp.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SliderFlags_AlwaysClamp, 'cache'):
    SliderFlags_AlwaysClamp.cache = SliderFlags_AlwaysClamp.func()
  return SliderFlags_AlwaysClamp.cache

@reapy.inside_reaper()
def SliderFlags_Logarithmic():
  if not hasattr(SliderFlags_Logarithmic, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_Logarithmic')
    SliderFlags_Logarithmic.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SliderFlags_Logarithmic, 'cache'):
    SliderFlags_Logarithmic.cache = SliderFlags_Logarithmic.func()
  return SliderFlags_Logarithmic.cache

@reapy.inside_reaper()
def SliderFlags_NoInput():
  if not hasattr(SliderFlags_NoInput, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_NoInput')
    SliderFlags_NoInput.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SliderFlags_NoInput, 'cache'):
    SliderFlags_NoInput.cache = SliderFlags_NoInput.func()
  return SliderFlags_NoInput.cache

@reapy.inside_reaper()
def SliderFlags_NoRoundToFormat():
  if not hasattr(SliderFlags_NoRoundToFormat, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_NoRoundToFormat')
    SliderFlags_NoRoundToFormat.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SliderFlags_NoRoundToFormat, 'cache'):
    SliderFlags_NoRoundToFormat.cache = SliderFlags_NoRoundToFormat.func()
  return SliderFlags_NoRoundToFormat.cache

@reapy.inside_reaper()
def SliderFlags_None():
  if not hasattr(SliderFlags_None, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_None')
    SliderFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SliderFlags_None, 'cache'):
    SliderFlags_None.cache = SliderFlags_None.func()
  return SliderFlags_None.cache

@reapy.inside_reaper()
def SliderInt(ctx, label, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderInt, 'func'):
    proc = rpr_getfp('ImGui_SliderInt')
    SliderInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(vInOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderInt.func(args[0], args[1], byref(args[2]), args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)
  return rval, int(args[2].value)

@reapy.inside_reaper()
def SliderInt2(ctx, label, v1InOut, v2InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderInt2, 'func'):
    proc = rpr_getfp('ImGui_SliderInt2')
    SliderInt2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderInt2.func(args[0], args[1], byref(args[2]), byref(args[3]), args[4], args[5], args[6], byref(args[7]) if args[7] != None else None)
  return rval, int(args[2].value), int(args[3].value)

@reapy.inside_reaper()
def SliderInt3(ctx, label, v1InOut, v2InOut, v3InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderInt3, 'func'):
    proc = rpr_getfp('ImGui_SliderInt3')
    SliderInt3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderInt3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value)

@reapy.inside_reaper()
def SliderInt4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(SliderInt4, 'func'):
    proc = rpr_getfp('ImGui_SliderInt4')
    SliderInt4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v4InOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = SliderInt4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), args[6], args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

@reapy.inside_reaper()
def SmallButton(ctx, label):
  if not hasattr(SmallButton, 'func'):
    proc = rpr_getfp('ImGui_SmallButton')
    SmallButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label))
  rval = SmallButton.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def SortDirection_Ascending():
  if not hasattr(SortDirection_Ascending, 'func'):
    proc = rpr_getfp('ImGui_SortDirection_Ascending')
    SortDirection_Ascending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SortDirection_Ascending, 'cache'):
    SortDirection_Ascending.cache = SortDirection_Ascending.func()
  return SortDirection_Ascending.cache

@reapy.inside_reaper()
def SortDirection_Descending():
  if not hasattr(SortDirection_Descending, 'func'):
    proc = rpr_getfp('ImGui_SortDirection_Descending')
    SortDirection_Descending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SortDirection_Descending, 'cache'):
    SortDirection_Descending.cache = SortDirection_Descending.func()
  return SortDirection_Descending.cache

@reapy.inside_reaper()
def SortDirection_None():
  if not hasattr(SortDirection_None, 'func'):
    proc = rpr_getfp('ImGui_SortDirection_None')
    SortDirection_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(SortDirection_None, 'cache'):
    SortDirection_None.cache = SortDirection_None.func()
  return SortDirection_None.cache

@reapy.inside_reaper()
def Spacing(ctx):
  if not hasattr(Spacing, 'func'):
    proc = rpr_getfp('ImGui_Spacing')
    Spacing.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  Spacing.func(args[0])

@reapy.inside_reaper()
def StyleVar_Alpha():
  if not hasattr(StyleVar_Alpha, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_Alpha')
    StyleVar_Alpha.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_Alpha, 'cache'):
    StyleVar_Alpha.cache = StyleVar_Alpha.func()
  return StyleVar_Alpha.cache

@reapy.inside_reaper()
def StyleVar_ButtonTextAlign():
  if not hasattr(StyleVar_ButtonTextAlign, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ButtonTextAlign')
    StyleVar_ButtonTextAlign.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ButtonTextAlign, 'cache'):
    StyleVar_ButtonTextAlign.cache = StyleVar_ButtonTextAlign.func()
  return StyleVar_ButtonTextAlign.cache

@reapy.inside_reaper()
def StyleVar_CellPadding():
  if not hasattr(StyleVar_CellPadding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_CellPadding')
    StyleVar_CellPadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_CellPadding, 'cache'):
    StyleVar_CellPadding.cache = StyleVar_CellPadding.func()
  return StyleVar_CellPadding.cache

@reapy.inside_reaper()
def StyleVar_ChildBorderSize():
  if not hasattr(StyleVar_ChildBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ChildBorderSize')
    StyleVar_ChildBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ChildBorderSize, 'cache'):
    StyleVar_ChildBorderSize.cache = StyleVar_ChildBorderSize.func()
  return StyleVar_ChildBorderSize.cache

@reapy.inside_reaper()
def StyleVar_ChildRounding():
  if not hasattr(StyleVar_ChildRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ChildRounding')
    StyleVar_ChildRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ChildRounding, 'cache'):
    StyleVar_ChildRounding.cache = StyleVar_ChildRounding.func()
  return StyleVar_ChildRounding.cache

@reapy.inside_reaper()
def StyleVar_DisabledAlpha():
  if not hasattr(StyleVar_DisabledAlpha, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_DisabledAlpha')
    StyleVar_DisabledAlpha.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_DisabledAlpha, 'cache'):
    StyleVar_DisabledAlpha.cache = StyleVar_DisabledAlpha.func()
  return StyleVar_DisabledAlpha.cache

@reapy.inside_reaper()
def StyleVar_FrameBorderSize():
  if not hasattr(StyleVar_FrameBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_FrameBorderSize')
    StyleVar_FrameBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_FrameBorderSize, 'cache'):
    StyleVar_FrameBorderSize.cache = StyleVar_FrameBorderSize.func()
  return StyleVar_FrameBorderSize.cache

@reapy.inside_reaper()
def StyleVar_FramePadding():
  if not hasattr(StyleVar_FramePadding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_FramePadding')
    StyleVar_FramePadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_FramePadding, 'cache'):
    StyleVar_FramePadding.cache = StyleVar_FramePadding.func()
  return StyleVar_FramePadding.cache

@reapy.inside_reaper()
def StyleVar_FrameRounding():
  if not hasattr(StyleVar_FrameRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_FrameRounding')
    StyleVar_FrameRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_FrameRounding, 'cache'):
    StyleVar_FrameRounding.cache = StyleVar_FrameRounding.func()
  return StyleVar_FrameRounding.cache

@reapy.inside_reaper()
def StyleVar_GrabMinSize():
  if not hasattr(StyleVar_GrabMinSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_GrabMinSize')
    StyleVar_GrabMinSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_GrabMinSize, 'cache'):
    StyleVar_GrabMinSize.cache = StyleVar_GrabMinSize.func()
  return StyleVar_GrabMinSize.cache

@reapy.inside_reaper()
def StyleVar_GrabRounding():
  if not hasattr(StyleVar_GrabRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_GrabRounding')
    StyleVar_GrabRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_GrabRounding, 'cache'):
    StyleVar_GrabRounding.cache = StyleVar_GrabRounding.func()
  return StyleVar_GrabRounding.cache

@reapy.inside_reaper()
def StyleVar_IndentSpacing():
  if not hasattr(StyleVar_IndentSpacing, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_IndentSpacing')
    StyleVar_IndentSpacing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_IndentSpacing, 'cache'):
    StyleVar_IndentSpacing.cache = StyleVar_IndentSpacing.func()
  return StyleVar_IndentSpacing.cache

@reapy.inside_reaper()
def StyleVar_ItemInnerSpacing():
  if not hasattr(StyleVar_ItemInnerSpacing, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ItemInnerSpacing')
    StyleVar_ItemInnerSpacing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ItemInnerSpacing, 'cache'):
    StyleVar_ItemInnerSpacing.cache = StyleVar_ItemInnerSpacing.func()
  return StyleVar_ItemInnerSpacing.cache

@reapy.inside_reaper()
def StyleVar_ItemSpacing():
  if not hasattr(StyleVar_ItemSpacing, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ItemSpacing')
    StyleVar_ItemSpacing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ItemSpacing, 'cache'):
    StyleVar_ItemSpacing.cache = StyleVar_ItemSpacing.func()
  return StyleVar_ItemSpacing.cache

@reapy.inside_reaper()
def StyleVar_PopupBorderSize():
  if not hasattr(StyleVar_PopupBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_PopupBorderSize')
    StyleVar_PopupBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_PopupBorderSize, 'cache'):
    StyleVar_PopupBorderSize.cache = StyleVar_PopupBorderSize.func()
  return StyleVar_PopupBorderSize.cache

@reapy.inside_reaper()
def StyleVar_PopupRounding():
  if not hasattr(StyleVar_PopupRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_PopupRounding')
    StyleVar_PopupRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_PopupRounding, 'cache'):
    StyleVar_PopupRounding.cache = StyleVar_PopupRounding.func()
  return StyleVar_PopupRounding.cache

@reapy.inside_reaper()
def StyleVar_ScrollbarRounding():
  if not hasattr(StyleVar_ScrollbarRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ScrollbarRounding')
    StyleVar_ScrollbarRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ScrollbarRounding, 'cache'):
    StyleVar_ScrollbarRounding.cache = StyleVar_ScrollbarRounding.func()
  return StyleVar_ScrollbarRounding.cache

@reapy.inside_reaper()
def StyleVar_ScrollbarSize():
  if not hasattr(StyleVar_ScrollbarSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ScrollbarSize')
    StyleVar_ScrollbarSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_ScrollbarSize, 'cache'):
    StyleVar_ScrollbarSize.cache = StyleVar_ScrollbarSize.func()
  return StyleVar_ScrollbarSize.cache

@reapy.inside_reaper()
def StyleVar_SelectableTextAlign():
  if not hasattr(StyleVar_SelectableTextAlign, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_SelectableTextAlign')
    StyleVar_SelectableTextAlign.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_SelectableTextAlign, 'cache'):
    StyleVar_SelectableTextAlign.cache = StyleVar_SelectableTextAlign.func()
  return StyleVar_SelectableTextAlign.cache

@reapy.inside_reaper()
def StyleVar_TabRounding():
  if not hasattr(StyleVar_TabRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_TabRounding')
    StyleVar_TabRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_TabRounding, 'cache'):
    StyleVar_TabRounding.cache = StyleVar_TabRounding.func()
  return StyleVar_TabRounding.cache

@reapy.inside_reaper()
def StyleVar_WindowBorderSize():
  if not hasattr(StyleVar_WindowBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowBorderSize')
    StyleVar_WindowBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_WindowBorderSize, 'cache'):
    StyleVar_WindowBorderSize.cache = StyleVar_WindowBorderSize.func()
  return StyleVar_WindowBorderSize.cache

@reapy.inside_reaper()
def StyleVar_WindowMinSize():
  if not hasattr(StyleVar_WindowMinSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowMinSize')
    StyleVar_WindowMinSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_WindowMinSize, 'cache'):
    StyleVar_WindowMinSize.cache = StyleVar_WindowMinSize.func()
  return StyleVar_WindowMinSize.cache

@reapy.inside_reaper()
def StyleVar_WindowPadding():
  if not hasattr(StyleVar_WindowPadding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowPadding')
    StyleVar_WindowPadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_WindowPadding, 'cache'):
    StyleVar_WindowPadding.cache = StyleVar_WindowPadding.func()
  return StyleVar_WindowPadding.cache

@reapy.inside_reaper()
def StyleVar_WindowRounding():
  if not hasattr(StyleVar_WindowRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowRounding')
    StyleVar_WindowRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_WindowRounding, 'cache'):
    StyleVar_WindowRounding.cache = StyleVar_WindowRounding.func()
  return StyleVar_WindowRounding.cache

@reapy.inside_reaper()
def StyleVar_WindowTitleAlign():
  if not hasattr(StyleVar_WindowTitleAlign, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowTitleAlign')
    StyleVar_WindowTitleAlign.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(StyleVar_WindowTitleAlign, 'cache'):
    StyleVar_WindowTitleAlign.cache = StyleVar_WindowTitleAlign.func()
  return StyleVar_WindowTitleAlign.cache

@reapy.inside_reaper()
def TabBarFlags_AutoSelectNewTabs():
  if not hasattr(TabBarFlags_AutoSelectNewTabs, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_AutoSelectNewTabs')
    TabBarFlags_AutoSelectNewTabs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_AutoSelectNewTabs, 'cache'):
    TabBarFlags_AutoSelectNewTabs.cache = TabBarFlags_AutoSelectNewTabs.func()
  return TabBarFlags_AutoSelectNewTabs.cache

@reapy.inside_reaper()
def TabBarFlags_FittingPolicyResizeDown():
  if not hasattr(TabBarFlags_FittingPolicyResizeDown, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_FittingPolicyResizeDown')
    TabBarFlags_FittingPolicyResizeDown.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_FittingPolicyResizeDown, 'cache'):
    TabBarFlags_FittingPolicyResizeDown.cache = TabBarFlags_FittingPolicyResizeDown.func()
  return TabBarFlags_FittingPolicyResizeDown.cache

@reapy.inside_reaper()
def TabBarFlags_FittingPolicyScroll():
  if not hasattr(TabBarFlags_FittingPolicyScroll, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_FittingPolicyScroll')
    TabBarFlags_FittingPolicyScroll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_FittingPolicyScroll, 'cache'):
    TabBarFlags_FittingPolicyScroll.cache = TabBarFlags_FittingPolicyScroll.func()
  return TabBarFlags_FittingPolicyScroll.cache

@reapy.inside_reaper()
def TabBarFlags_NoCloseWithMiddleMouseButton():
  if not hasattr(TabBarFlags_NoCloseWithMiddleMouseButton, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_NoCloseWithMiddleMouseButton')
    TabBarFlags_NoCloseWithMiddleMouseButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_NoCloseWithMiddleMouseButton, 'cache'):
    TabBarFlags_NoCloseWithMiddleMouseButton.cache = TabBarFlags_NoCloseWithMiddleMouseButton.func()
  return TabBarFlags_NoCloseWithMiddleMouseButton.cache

@reapy.inside_reaper()
def TabBarFlags_NoTabListScrollingButtons():
  if not hasattr(TabBarFlags_NoTabListScrollingButtons, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_NoTabListScrollingButtons')
    TabBarFlags_NoTabListScrollingButtons.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_NoTabListScrollingButtons, 'cache'):
    TabBarFlags_NoTabListScrollingButtons.cache = TabBarFlags_NoTabListScrollingButtons.func()
  return TabBarFlags_NoTabListScrollingButtons.cache

@reapy.inside_reaper()
def TabBarFlags_NoTooltip():
  if not hasattr(TabBarFlags_NoTooltip, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_NoTooltip')
    TabBarFlags_NoTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_NoTooltip, 'cache'):
    TabBarFlags_NoTooltip.cache = TabBarFlags_NoTooltip.func()
  return TabBarFlags_NoTooltip.cache

@reapy.inside_reaper()
def TabBarFlags_None():
  if not hasattr(TabBarFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_None')
    TabBarFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_None, 'cache'):
    TabBarFlags_None.cache = TabBarFlags_None.func()
  return TabBarFlags_None.cache

@reapy.inside_reaper()
def TabBarFlags_Reorderable():
  if not hasattr(TabBarFlags_Reorderable, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_Reorderable')
    TabBarFlags_Reorderable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_Reorderable, 'cache'):
    TabBarFlags_Reorderable.cache = TabBarFlags_Reorderable.func()
  return TabBarFlags_Reorderable.cache

@reapy.inside_reaper()
def TabBarFlags_TabListPopupButton():
  if not hasattr(TabBarFlags_TabListPopupButton, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_TabListPopupButton')
    TabBarFlags_TabListPopupButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabBarFlags_TabListPopupButton, 'cache'):
    TabBarFlags_TabListPopupButton.cache = TabBarFlags_TabListPopupButton.func()
  return TabBarFlags_TabListPopupButton.cache

@reapy.inside_reaper()
def TabItemButton(ctx, label, flagsInOptional = None):
  if not hasattr(TabItemButton, 'func'):
    proc = rpr_getfp('ImGui_TabItemButton')
    TabItemButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = TabItemButton.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def TabItemFlags_Leading():
  if not hasattr(TabItemFlags_Leading, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_Leading')
    TabItemFlags_Leading.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_Leading, 'cache'):
    TabItemFlags_Leading.cache = TabItemFlags_Leading.func()
  return TabItemFlags_Leading.cache

@reapy.inside_reaper()
def TabItemFlags_NoCloseWithMiddleMouseButton():
  if not hasattr(TabItemFlags_NoCloseWithMiddleMouseButton, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoCloseWithMiddleMouseButton')
    TabItemFlags_NoCloseWithMiddleMouseButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_NoCloseWithMiddleMouseButton, 'cache'):
    TabItemFlags_NoCloseWithMiddleMouseButton.cache = TabItemFlags_NoCloseWithMiddleMouseButton.func()
  return TabItemFlags_NoCloseWithMiddleMouseButton.cache

@reapy.inside_reaper()
def TabItemFlags_NoPushId():
  if not hasattr(TabItemFlags_NoPushId, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoPushId')
    TabItemFlags_NoPushId.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_NoPushId, 'cache'):
    TabItemFlags_NoPushId.cache = TabItemFlags_NoPushId.func()
  return TabItemFlags_NoPushId.cache

@reapy.inside_reaper()
def TabItemFlags_NoReorder():
  if not hasattr(TabItemFlags_NoReorder, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoReorder')
    TabItemFlags_NoReorder.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_NoReorder, 'cache'):
    TabItemFlags_NoReorder.cache = TabItemFlags_NoReorder.func()
  return TabItemFlags_NoReorder.cache

@reapy.inside_reaper()
def TabItemFlags_NoTooltip():
  if not hasattr(TabItemFlags_NoTooltip, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoTooltip')
    TabItemFlags_NoTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_NoTooltip, 'cache'):
    TabItemFlags_NoTooltip.cache = TabItemFlags_NoTooltip.func()
  return TabItemFlags_NoTooltip.cache

@reapy.inside_reaper()
def TabItemFlags_None():
  if not hasattr(TabItemFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_None')
    TabItemFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_None, 'cache'):
    TabItemFlags_None.cache = TabItemFlags_None.func()
  return TabItemFlags_None.cache

@reapy.inside_reaper()
def TabItemFlags_SetSelected():
  if not hasattr(TabItemFlags_SetSelected, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_SetSelected')
    TabItemFlags_SetSelected.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_SetSelected, 'cache'):
    TabItemFlags_SetSelected.cache = TabItemFlags_SetSelected.func()
  return TabItemFlags_SetSelected.cache

@reapy.inside_reaper()
def TabItemFlags_Trailing():
  if not hasattr(TabItemFlags_Trailing, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_Trailing')
    TabItemFlags_Trailing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_Trailing, 'cache'):
    TabItemFlags_Trailing.cache = TabItemFlags_Trailing.func()
  return TabItemFlags_Trailing.cache

@reapy.inside_reaper()
def TabItemFlags_UnsavedDocument():
  if not hasattr(TabItemFlags_UnsavedDocument, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_UnsavedDocument')
    TabItemFlags_UnsavedDocument.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TabItemFlags_UnsavedDocument, 'cache'):
    TabItemFlags_UnsavedDocument.cache = TabItemFlags_UnsavedDocument.func()
  return TabItemFlags_UnsavedDocument.cache

@reapy.inside_reaper()
def TableBgTarget_CellBg():
  if not hasattr(TableBgTarget_CellBg, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_CellBg')
    TableBgTarget_CellBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableBgTarget_CellBg, 'cache'):
    TableBgTarget_CellBg.cache = TableBgTarget_CellBg.func()
  return TableBgTarget_CellBg.cache

@reapy.inside_reaper()
def TableBgTarget_None():
  if not hasattr(TableBgTarget_None, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_None')
    TableBgTarget_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableBgTarget_None, 'cache'):
    TableBgTarget_None.cache = TableBgTarget_None.func()
  return TableBgTarget_None.cache

@reapy.inside_reaper()
def TableBgTarget_RowBg0():
  if not hasattr(TableBgTarget_RowBg0, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_RowBg0')
    TableBgTarget_RowBg0.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableBgTarget_RowBg0, 'cache'):
    TableBgTarget_RowBg0.cache = TableBgTarget_RowBg0.func()
  return TableBgTarget_RowBg0.cache

@reapy.inside_reaper()
def TableBgTarget_RowBg1():
  if not hasattr(TableBgTarget_RowBg1, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_RowBg1')
    TableBgTarget_RowBg1.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableBgTarget_RowBg1, 'cache'):
    TableBgTarget_RowBg1.cache = TableBgTarget_RowBg1.func()
  return TableBgTarget_RowBg1.cache

@reapy.inside_reaper()
def TableColumnFlags_DefaultHide():
  if not hasattr(TableColumnFlags_DefaultHide, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_DefaultHide')
    TableColumnFlags_DefaultHide.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_DefaultHide, 'cache'):
    TableColumnFlags_DefaultHide.cache = TableColumnFlags_DefaultHide.func()
  return TableColumnFlags_DefaultHide.cache

@reapy.inside_reaper()
def TableColumnFlags_DefaultSort():
  if not hasattr(TableColumnFlags_DefaultSort, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_DefaultSort')
    TableColumnFlags_DefaultSort.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_DefaultSort, 'cache'):
    TableColumnFlags_DefaultSort.cache = TableColumnFlags_DefaultSort.func()
  return TableColumnFlags_DefaultSort.cache

@reapy.inside_reaper()
def TableColumnFlags_Disabled():
  if not hasattr(TableColumnFlags_Disabled, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_Disabled')
    TableColumnFlags_Disabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_Disabled, 'cache'):
    TableColumnFlags_Disabled.cache = TableColumnFlags_Disabled.func()
  return TableColumnFlags_Disabled.cache

@reapy.inside_reaper()
def TableColumnFlags_IndentDisable():
  if not hasattr(TableColumnFlags_IndentDisable, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IndentDisable')
    TableColumnFlags_IndentDisable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_IndentDisable, 'cache'):
    TableColumnFlags_IndentDisable.cache = TableColumnFlags_IndentDisable.func()
  return TableColumnFlags_IndentDisable.cache

@reapy.inside_reaper()
def TableColumnFlags_IndentEnable():
  if not hasattr(TableColumnFlags_IndentEnable, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IndentEnable')
    TableColumnFlags_IndentEnable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_IndentEnable, 'cache'):
    TableColumnFlags_IndentEnable.cache = TableColumnFlags_IndentEnable.func()
  return TableColumnFlags_IndentEnable.cache

@reapy.inside_reaper()
def TableColumnFlags_IsEnabled():
  if not hasattr(TableColumnFlags_IsEnabled, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsEnabled')
    TableColumnFlags_IsEnabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_IsEnabled, 'cache'):
    TableColumnFlags_IsEnabled.cache = TableColumnFlags_IsEnabled.func()
  return TableColumnFlags_IsEnabled.cache

@reapy.inside_reaper()
def TableColumnFlags_IsHovered():
  if not hasattr(TableColumnFlags_IsHovered, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsHovered')
    TableColumnFlags_IsHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_IsHovered, 'cache'):
    TableColumnFlags_IsHovered.cache = TableColumnFlags_IsHovered.func()
  return TableColumnFlags_IsHovered.cache

@reapy.inside_reaper()
def TableColumnFlags_IsSorted():
  if not hasattr(TableColumnFlags_IsSorted, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsSorted')
    TableColumnFlags_IsSorted.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_IsSorted, 'cache'):
    TableColumnFlags_IsSorted.cache = TableColumnFlags_IsSorted.func()
  return TableColumnFlags_IsSorted.cache

@reapy.inside_reaper()
def TableColumnFlags_IsVisible():
  if not hasattr(TableColumnFlags_IsVisible, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsVisible')
    TableColumnFlags_IsVisible.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_IsVisible, 'cache'):
    TableColumnFlags_IsVisible.cache = TableColumnFlags_IsVisible.func()
  return TableColumnFlags_IsVisible.cache

@reapy.inside_reaper()
def TableColumnFlags_NoClip():
  if not hasattr(TableColumnFlags_NoClip, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoClip')
    TableColumnFlags_NoClip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoClip, 'cache'):
    TableColumnFlags_NoClip.cache = TableColumnFlags_NoClip.func()
  return TableColumnFlags_NoClip.cache

@reapy.inside_reaper()
def TableColumnFlags_NoHeaderLabel():
  if not hasattr(TableColumnFlags_NoHeaderLabel, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoHeaderLabel')
    TableColumnFlags_NoHeaderLabel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoHeaderLabel, 'cache'):
    TableColumnFlags_NoHeaderLabel.cache = TableColumnFlags_NoHeaderLabel.func()
  return TableColumnFlags_NoHeaderLabel.cache

@reapy.inside_reaper()
def TableColumnFlags_NoHeaderWidth():
  if not hasattr(TableColumnFlags_NoHeaderWidth, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoHeaderWidth')
    TableColumnFlags_NoHeaderWidth.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoHeaderWidth, 'cache'):
    TableColumnFlags_NoHeaderWidth.cache = TableColumnFlags_NoHeaderWidth.func()
  return TableColumnFlags_NoHeaderWidth.cache

@reapy.inside_reaper()
def TableColumnFlags_NoHide():
  if not hasattr(TableColumnFlags_NoHide, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoHide')
    TableColumnFlags_NoHide.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoHide, 'cache'):
    TableColumnFlags_NoHide.cache = TableColumnFlags_NoHide.func()
  return TableColumnFlags_NoHide.cache

@reapy.inside_reaper()
def TableColumnFlags_NoReorder():
  if not hasattr(TableColumnFlags_NoReorder, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoReorder')
    TableColumnFlags_NoReorder.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoReorder, 'cache'):
    TableColumnFlags_NoReorder.cache = TableColumnFlags_NoReorder.func()
  return TableColumnFlags_NoReorder.cache

@reapy.inside_reaper()
def TableColumnFlags_NoResize():
  if not hasattr(TableColumnFlags_NoResize, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoResize')
    TableColumnFlags_NoResize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoResize, 'cache'):
    TableColumnFlags_NoResize.cache = TableColumnFlags_NoResize.func()
  return TableColumnFlags_NoResize.cache

@reapy.inside_reaper()
def TableColumnFlags_NoSort():
  if not hasattr(TableColumnFlags_NoSort, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoSort')
    TableColumnFlags_NoSort.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoSort, 'cache'):
    TableColumnFlags_NoSort.cache = TableColumnFlags_NoSort.func()
  return TableColumnFlags_NoSort.cache

@reapy.inside_reaper()
def TableColumnFlags_NoSortAscending():
  if not hasattr(TableColumnFlags_NoSortAscending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoSortAscending')
    TableColumnFlags_NoSortAscending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoSortAscending, 'cache'):
    TableColumnFlags_NoSortAscending.cache = TableColumnFlags_NoSortAscending.func()
  return TableColumnFlags_NoSortAscending.cache

@reapy.inside_reaper()
def TableColumnFlags_NoSortDescending():
  if not hasattr(TableColumnFlags_NoSortDescending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoSortDescending')
    TableColumnFlags_NoSortDescending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_NoSortDescending, 'cache'):
    TableColumnFlags_NoSortDescending.cache = TableColumnFlags_NoSortDescending.func()
  return TableColumnFlags_NoSortDescending.cache

@reapy.inside_reaper()
def TableColumnFlags_None():
  if not hasattr(TableColumnFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_None')
    TableColumnFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_None, 'cache'):
    TableColumnFlags_None.cache = TableColumnFlags_None.func()
  return TableColumnFlags_None.cache

@reapy.inside_reaper()
def TableColumnFlags_PreferSortAscending():
  if not hasattr(TableColumnFlags_PreferSortAscending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_PreferSortAscending')
    TableColumnFlags_PreferSortAscending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_PreferSortAscending, 'cache'):
    TableColumnFlags_PreferSortAscending.cache = TableColumnFlags_PreferSortAscending.func()
  return TableColumnFlags_PreferSortAscending.cache

@reapy.inside_reaper()
def TableColumnFlags_PreferSortDescending():
  if not hasattr(TableColumnFlags_PreferSortDescending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_PreferSortDescending')
    TableColumnFlags_PreferSortDescending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_PreferSortDescending, 'cache'):
    TableColumnFlags_PreferSortDescending.cache = TableColumnFlags_PreferSortDescending.func()
  return TableColumnFlags_PreferSortDescending.cache

@reapy.inside_reaper()
def TableColumnFlags_WidthFixed():
  if not hasattr(TableColumnFlags_WidthFixed, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_WidthFixed')
    TableColumnFlags_WidthFixed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_WidthFixed, 'cache'):
    TableColumnFlags_WidthFixed.cache = TableColumnFlags_WidthFixed.func()
  return TableColumnFlags_WidthFixed.cache

@reapy.inside_reaper()
def TableColumnFlags_WidthStretch():
  if not hasattr(TableColumnFlags_WidthStretch, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_WidthStretch')
    TableColumnFlags_WidthStretch.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableColumnFlags_WidthStretch, 'cache'):
    TableColumnFlags_WidthStretch.cache = TableColumnFlags_WidthStretch.func()
  return TableColumnFlags_WidthStretch.cache

@reapy.inside_reaper()
def TableFlags_Borders():
  if not hasattr(TableFlags_Borders, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Borders')
    TableFlags_Borders.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_Borders, 'cache'):
    TableFlags_Borders.cache = TableFlags_Borders.func()
  return TableFlags_Borders.cache

@reapy.inside_reaper()
def TableFlags_BordersH():
  if not hasattr(TableFlags_BordersH, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersH')
    TableFlags_BordersH.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersH, 'cache'):
    TableFlags_BordersH.cache = TableFlags_BordersH.func()
  return TableFlags_BordersH.cache

@reapy.inside_reaper()
def TableFlags_BordersInner():
  if not hasattr(TableFlags_BordersInner, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersInner')
    TableFlags_BordersInner.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersInner, 'cache'):
    TableFlags_BordersInner.cache = TableFlags_BordersInner.func()
  return TableFlags_BordersInner.cache

@reapy.inside_reaper()
def TableFlags_BordersInnerH():
  if not hasattr(TableFlags_BordersInnerH, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersInnerH')
    TableFlags_BordersInnerH.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersInnerH, 'cache'):
    TableFlags_BordersInnerH.cache = TableFlags_BordersInnerH.func()
  return TableFlags_BordersInnerH.cache

@reapy.inside_reaper()
def TableFlags_BordersInnerV():
  if not hasattr(TableFlags_BordersInnerV, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersInnerV')
    TableFlags_BordersInnerV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersInnerV, 'cache'):
    TableFlags_BordersInnerV.cache = TableFlags_BordersInnerV.func()
  return TableFlags_BordersInnerV.cache

@reapy.inside_reaper()
def TableFlags_BordersOuter():
  if not hasattr(TableFlags_BordersOuter, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersOuter')
    TableFlags_BordersOuter.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersOuter, 'cache'):
    TableFlags_BordersOuter.cache = TableFlags_BordersOuter.func()
  return TableFlags_BordersOuter.cache

@reapy.inside_reaper()
def TableFlags_BordersOuterH():
  if not hasattr(TableFlags_BordersOuterH, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersOuterH')
    TableFlags_BordersOuterH.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersOuterH, 'cache'):
    TableFlags_BordersOuterH.cache = TableFlags_BordersOuterH.func()
  return TableFlags_BordersOuterH.cache

@reapy.inside_reaper()
def TableFlags_BordersOuterV():
  if not hasattr(TableFlags_BordersOuterV, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersOuterV')
    TableFlags_BordersOuterV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersOuterV, 'cache'):
    TableFlags_BordersOuterV.cache = TableFlags_BordersOuterV.func()
  return TableFlags_BordersOuterV.cache

@reapy.inside_reaper()
def TableFlags_BordersV():
  if not hasattr(TableFlags_BordersV, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersV')
    TableFlags_BordersV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_BordersV, 'cache'):
    TableFlags_BordersV.cache = TableFlags_BordersV.func()
  return TableFlags_BordersV.cache

@reapy.inside_reaper()
def TableFlags_ContextMenuInBody():
  if not hasattr(TableFlags_ContextMenuInBody, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_ContextMenuInBody')
    TableFlags_ContextMenuInBody.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_ContextMenuInBody, 'cache'):
    TableFlags_ContextMenuInBody.cache = TableFlags_ContextMenuInBody.func()
  return TableFlags_ContextMenuInBody.cache

@reapy.inside_reaper()
def TableFlags_Hideable():
  if not hasattr(TableFlags_Hideable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Hideable')
    TableFlags_Hideable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_Hideable, 'cache'):
    TableFlags_Hideable.cache = TableFlags_Hideable.func()
  return TableFlags_Hideable.cache

@reapy.inside_reaper()
def TableFlags_NoClip():
  if not hasattr(TableFlags_NoClip, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoClip')
    TableFlags_NoClip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoClip, 'cache'):
    TableFlags_NoClip.cache = TableFlags_NoClip.func()
  return TableFlags_NoClip.cache

@reapy.inside_reaper()
def TableFlags_NoHostExtendX():
  if not hasattr(TableFlags_NoHostExtendX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoHostExtendX')
    TableFlags_NoHostExtendX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoHostExtendX, 'cache'):
    TableFlags_NoHostExtendX.cache = TableFlags_NoHostExtendX.func()
  return TableFlags_NoHostExtendX.cache

@reapy.inside_reaper()
def TableFlags_NoHostExtendY():
  if not hasattr(TableFlags_NoHostExtendY, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoHostExtendY')
    TableFlags_NoHostExtendY.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoHostExtendY, 'cache'):
    TableFlags_NoHostExtendY.cache = TableFlags_NoHostExtendY.func()
  return TableFlags_NoHostExtendY.cache

@reapy.inside_reaper()
def TableFlags_NoKeepColumnsVisible():
  if not hasattr(TableFlags_NoKeepColumnsVisible, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoKeepColumnsVisible')
    TableFlags_NoKeepColumnsVisible.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoKeepColumnsVisible, 'cache'):
    TableFlags_NoKeepColumnsVisible.cache = TableFlags_NoKeepColumnsVisible.func()
  return TableFlags_NoKeepColumnsVisible.cache

@reapy.inside_reaper()
def TableFlags_NoPadInnerX():
  if not hasattr(TableFlags_NoPadInnerX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoPadInnerX')
    TableFlags_NoPadInnerX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoPadInnerX, 'cache'):
    TableFlags_NoPadInnerX.cache = TableFlags_NoPadInnerX.func()
  return TableFlags_NoPadInnerX.cache

@reapy.inside_reaper()
def TableFlags_NoPadOuterX():
  if not hasattr(TableFlags_NoPadOuterX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoPadOuterX')
    TableFlags_NoPadOuterX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoPadOuterX, 'cache'):
    TableFlags_NoPadOuterX.cache = TableFlags_NoPadOuterX.func()
  return TableFlags_NoPadOuterX.cache

@reapy.inside_reaper()
def TableFlags_NoSavedSettings():
  if not hasattr(TableFlags_NoSavedSettings, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoSavedSettings')
    TableFlags_NoSavedSettings.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_NoSavedSettings, 'cache'):
    TableFlags_NoSavedSettings.cache = TableFlags_NoSavedSettings.func()
  return TableFlags_NoSavedSettings.cache

@reapy.inside_reaper()
def TableFlags_None():
  if not hasattr(TableFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_None')
    TableFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_None, 'cache'):
    TableFlags_None.cache = TableFlags_None.func()
  return TableFlags_None.cache

@reapy.inside_reaper()
def TableFlags_PadOuterX():
  if not hasattr(TableFlags_PadOuterX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_PadOuterX')
    TableFlags_PadOuterX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_PadOuterX, 'cache'):
    TableFlags_PadOuterX.cache = TableFlags_PadOuterX.func()
  return TableFlags_PadOuterX.cache

@reapy.inside_reaper()
def TableFlags_PreciseWidths():
  if not hasattr(TableFlags_PreciseWidths, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_PreciseWidths')
    TableFlags_PreciseWidths.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_PreciseWidths, 'cache'):
    TableFlags_PreciseWidths.cache = TableFlags_PreciseWidths.func()
  return TableFlags_PreciseWidths.cache

@reapy.inside_reaper()
def TableFlags_Reorderable():
  if not hasattr(TableFlags_Reorderable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Reorderable')
    TableFlags_Reorderable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_Reorderable, 'cache'):
    TableFlags_Reorderable.cache = TableFlags_Reorderable.func()
  return TableFlags_Reorderable.cache

@reapy.inside_reaper()
def TableFlags_Resizable():
  if not hasattr(TableFlags_Resizable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Resizable')
    TableFlags_Resizable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_Resizable, 'cache'):
    TableFlags_Resizable.cache = TableFlags_Resizable.func()
  return TableFlags_Resizable.cache

@reapy.inside_reaper()
def TableFlags_RowBg():
  if not hasattr(TableFlags_RowBg, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_RowBg')
    TableFlags_RowBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_RowBg, 'cache'):
    TableFlags_RowBg.cache = TableFlags_RowBg.func()
  return TableFlags_RowBg.cache

@reapy.inside_reaper()
def TableFlags_ScrollX():
  if not hasattr(TableFlags_ScrollX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_ScrollX')
    TableFlags_ScrollX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_ScrollX, 'cache'):
    TableFlags_ScrollX.cache = TableFlags_ScrollX.func()
  return TableFlags_ScrollX.cache

@reapy.inside_reaper()
def TableFlags_ScrollY():
  if not hasattr(TableFlags_ScrollY, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_ScrollY')
    TableFlags_ScrollY.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_ScrollY, 'cache'):
    TableFlags_ScrollY.cache = TableFlags_ScrollY.func()
  return TableFlags_ScrollY.cache

@reapy.inside_reaper()
def TableFlags_SizingFixedFit():
  if not hasattr(TableFlags_SizingFixedFit, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingFixedFit')
    TableFlags_SizingFixedFit.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_SizingFixedFit, 'cache'):
    TableFlags_SizingFixedFit.cache = TableFlags_SizingFixedFit.func()
  return TableFlags_SizingFixedFit.cache

@reapy.inside_reaper()
def TableFlags_SizingFixedSame():
  if not hasattr(TableFlags_SizingFixedSame, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingFixedSame')
    TableFlags_SizingFixedSame.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_SizingFixedSame, 'cache'):
    TableFlags_SizingFixedSame.cache = TableFlags_SizingFixedSame.func()
  return TableFlags_SizingFixedSame.cache

@reapy.inside_reaper()
def TableFlags_SizingStretchProp():
  if not hasattr(TableFlags_SizingStretchProp, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingStretchProp')
    TableFlags_SizingStretchProp.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_SizingStretchProp, 'cache'):
    TableFlags_SizingStretchProp.cache = TableFlags_SizingStretchProp.func()
  return TableFlags_SizingStretchProp.cache

@reapy.inside_reaper()
def TableFlags_SizingStretchSame():
  if not hasattr(TableFlags_SizingStretchSame, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingStretchSame')
    TableFlags_SizingStretchSame.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_SizingStretchSame, 'cache'):
    TableFlags_SizingStretchSame.cache = TableFlags_SizingStretchSame.func()
  return TableFlags_SizingStretchSame.cache

@reapy.inside_reaper()
def TableFlags_SortMulti():
  if not hasattr(TableFlags_SortMulti, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SortMulti')
    TableFlags_SortMulti.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_SortMulti, 'cache'):
    TableFlags_SortMulti.cache = TableFlags_SortMulti.func()
  return TableFlags_SortMulti.cache

@reapy.inside_reaper()
def TableFlags_SortTristate():
  if not hasattr(TableFlags_SortTristate, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SortTristate')
    TableFlags_SortTristate.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_SortTristate, 'cache'):
    TableFlags_SortTristate.cache = TableFlags_SortTristate.func()
  return TableFlags_SortTristate.cache

@reapy.inside_reaper()
def TableFlags_Sortable():
  if not hasattr(TableFlags_Sortable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Sortable')
    TableFlags_Sortable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableFlags_Sortable, 'cache'):
    TableFlags_Sortable.cache = TableFlags_Sortable.func()
  return TableFlags_Sortable.cache

@reapy.inside_reaper()
def TableGetColumnCount(ctx):
  if not hasattr(TableGetColumnCount, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnCount')
    TableGetColumnCount.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = TableGetColumnCount.func(args[0])
  return rval

@reapy.inside_reaper()
def TableGetColumnFlags(ctx, column_nInOptional = None):
  if not hasattr(TableGetColumnFlags, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnFlags')
    TableGetColumnFlags.func = CFUNCTYPE(c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(column_nInOptional) if column_nInOptional != None else None)
  rval = TableGetColumnFlags.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

@reapy.inside_reaper()
def TableGetColumnIndex(ctx):
  if not hasattr(TableGetColumnIndex, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnIndex')
    TableGetColumnIndex.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = TableGetColumnIndex.func(args[0])
  return rval

@reapy.inside_reaper()
def TableGetColumnName(ctx, column_nInOptional = None):
  if not hasattr(TableGetColumnName, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnName')
    TableGetColumnName.func = CFUNCTYPE(c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(column_nInOptional) if column_nInOptional != None else None)
  rval = TableGetColumnName.func(args[0], byref(args[1]) if args[1] != None else None)
  return str(rval.decode())

@reapy.inside_reaper()
def TableGetColumnSortSpecs(ctx, id, column_user_idOut = None, column_indexOut = None, sort_orderOut = None, sort_directionOut = None):
  if not hasattr(TableGetColumnSortSpecs, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnSortSpecs')
    TableGetColumnSortSpecs.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(id), c_int(column_user_idOut if column_user_idOut != None else 0), c_int(column_indexOut if column_indexOut != None else 0), c_int(sort_orderOut if sort_orderOut != None else 0), c_int(sort_directionOut if sort_directionOut != None else 0))
  rval = TableGetColumnSortSpecs.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]))
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

@reapy.inside_reaper()
def TableGetRowIndex(ctx):
  if not hasattr(TableGetRowIndex, 'func'):
    proc = rpr_getfp('ImGui_TableGetRowIndex')
    TableGetRowIndex.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = TableGetRowIndex.func(args[0])
  return rval

@reapy.inside_reaper()
def TableHeader(ctx, label):
  if not hasattr(TableHeader, 'func'):
    proc = rpr_getfp('ImGui_TableHeader')
    TableHeader.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label))
  TableHeader.func(args[0], args[1])

@reapy.inside_reaper()
def TableHeadersRow(ctx):
  if not hasattr(TableHeadersRow, 'func'):
    proc = rpr_getfp('ImGui_TableHeadersRow')
    TableHeadersRow.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  TableHeadersRow.func(args[0])

@reapy.inside_reaper()
def TableNeedSort(ctx, has_specsOut = None):
  if not hasattr(TableNeedSort, 'func'):
    proc = rpr_getfp('ImGui_TableNeedSort')
    TableNeedSort.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_bool(has_specsOut if has_specsOut != None else 0))
  rval = TableNeedSort.func(args[0], byref(args[1]))
  return rval, int(args[1].value)

@reapy.inside_reaper()
def TableNextColumn(ctx):
  if not hasattr(TableNextColumn, 'func'):
    proc = rpr_getfp('ImGui_TableNextColumn')
    TableNextColumn.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  rval = TableNextColumn.func(args[0])
  return rval

@reapy.inside_reaper()
def TableNextRow(ctx, row_flagsInOptional = None, min_row_heightInOptional = None):
  if not hasattr(TableNextRow, 'func'):
    proc = rpr_getfp('ImGui_TableNextRow')
    TableNextRow.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(row_flagsInOptional) if row_flagsInOptional != None else None, c_double(min_row_heightInOptional) if min_row_heightInOptional != None else None)
  TableNextRow.func(args[0], byref(args[1]) if args[1] != None else None, byref(args[2]) if args[2] != None else None)

@reapy.inside_reaper()
def TableRowFlags_Headers():
  if not hasattr(TableRowFlags_Headers, 'func'):
    proc = rpr_getfp('ImGui_TableRowFlags_Headers')
    TableRowFlags_Headers.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableRowFlags_Headers, 'cache'):
    TableRowFlags_Headers.cache = TableRowFlags_Headers.func()
  return TableRowFlags_Headers.cache

@reapy.inside_reaper()
def TableRowFlags_None():
  if not hasattr(TableRowFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TableRowFlags_None')
    TableRowFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TableRowFlags_None, 'cache'):
    TableRowFlags_None.cache = TableRowFlags_None.func()
  return TableRowFlags_None.cache

@reapy.inside_reaper()
def TableSetBgColor(ctx, target, color_rgba, column_nInOptional = None):
  if not hasattr(TableSetBgColor, 'func'):
    proc = rpr_getfp('ImGui_TableSetBgColor')
    TableSetBgColor.func = CFUNCTYPE(None, c_void_p, c_int, c_int, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(target), c_int(color_rgba), c_int(column_nInOptional) if column_nInOptional != None else None)
  TableSetBgColor.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

@reapy.inside_reaper()
def TableSetColumnEnabled(ctx, column_n, v):
  if not hasattr(TableSetColumnEnabled, 'func'):
    proc = rpr_getfp('ImGui_TableSetColumnEnabled')
    TableSetColumnEnabled.func = CFUNCTYPE(None, c_void_p, c_int, c_bool)(proc)
  args = (rpr_packp('Context*', ctx), c_int(column_n), c_bool(v))
  TableSetColumnEnabled.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def TableSetColumnIndex(ctx, column_n):
  if not hasattr(TableSetColumnIndex, 'func'):
    proc = rpr_getfp('ImGui_TableSetColumnIndex')
    TableSetColumnIndex.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(column_n))
  rval = TableSetColumnIndex.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def TableSetupColumn(ctx, label, flagsInOptional = None, init_width_or_weightInOptional = None, user_idInOptional = None):
  if not hasattr(TableSetupColumn, 'func'):
    proc = rpr_getfp('ImGui_TableSetupColumn')
    TableSetupColumn.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(init_width_or_weightInOptional) if init_width_or_weightInOptional != None else None, c_int(user_idInOptional) if user_idInOptional != None else None)
  TableSetupColumn.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)

@reapy.inside_reaper()
def TableSetupScrollFreeze(ctx, cols, rows):
  if not hasattr(TableSetupScrollFreeze, 'func'):
    proc = rpr_getfp('ImGui_TableSetupScrollFreeze')
    TableSetupScrollFreeze.func = CFUNCTYPE(None, c_void_p, c_int, c_int)(proc)
  args = (rpr_packp('Context*', ctx), c_int(cols), c_int(rows))
  TableSetupScrollFreeze.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def Text(ctx, text):
  if not hasattr(Text, 'func'):
    proc = rpr_getfp('ImGui_Text')
    Text.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  Text.func(args[0], args[1])

@reapy.inside_reaper()
def TextColored(ctx, col_rgba, text):
  if not hasattr(TextColored, 'func'):
    proc = rpr_getfp('ImGui_TextColored')
    TextColored.func = CFUNCTYPE(None, c_void_p, c_int, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), c_int(col_rgba), rpr_packsc(text))
  TextColored.func(args[0], args[1], args[2])

@reapy.inside_reaper()
def TextDisabled(ctx, text):
  if not hasattr(TextDisabled, 'func'):
    proc = rpr_getfp('ImGui_TextDisabled')
    TextDisabled.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  TextDisabled.func(args[0], args[1])

@reapy.inside_reaper()
def TextFilter_Clear(filter):
  if not hasattr(TextFilter_Clear, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Clear')
    TextFilter_Clear.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('TextFilter*', filter),)
  TextFilter_Clear.func(args[0])

@reapy.inside_reaper()
def TextFilter_Draw(filter, ctx, labelInOptional = None, widthInOptional = None):
  if not hasattr(TextFilter_Draw, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Draw')
    TextFilter_Draw.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('TextFilter*', filter), rpr_packp('Context*', ctx), rpr_packsc(labelInOptional) if labelInOptional != None else None, c_double(widthInOptional) if widthInOptional != None else None)
  rval = TextFilter_Draw.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

@reapy.inside_reaper()
def TextFilter_Get(filter):
  if not hasattr(TextFilter_Get, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Get')
    TextFilter_Get.func = CFUNCTYPE(c_char_p, c_void_p)(proc)
  args = (rpr_packp('TextFilter*', filter),)
  rval = TextFilter_Get.func(args[0])
  return str(rval.decode())

@reapy.inside_reaper()
def TextFilter_IsActive(filter):
  if not hasattr(TextFilter_IsActive, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_IsActive')
    TextFilter_IsActive.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('TextFilter*', filter),)
  rval = TextFilter_IsActive.func(args[0])
  return rval

@reapy.inside_reaper()
def TextFilter_PassFilter(filter, text):
  if not hasattr(TextFilter_PassFilter, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_PassFilter')
    TextFilter_PassFilter.func = CFUNCTYPE(c_bool, c_void_p, c_char_p)(proc)
  args = (rpr_packp('TextFilter*', filter), rpr_packsc(text))
  rval = TextFilter_PassFilter.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def TextFilter_Set(filter, filter_text):
  if not hasattr(TextFilter_Set, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Set')
    TextFilter_Set.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('TextFilter*', filter), rpr_packsc(filter_text))
  TextFilter_Set.func(args[0], args[1])

@reapy.inside_reaper()
def TextWrapped(ctx, text):
  if not hasattr(TextWrapped, 'func'):
    proc = rpr_getfp('ImGui_TextWrapped')
    TextWrapped.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(text))
  TextWrapped.func(args[0], args[1])

@reapy.inside_reaper()
def TreeNode(ctx, label, flagsInOptional = None):
  if not hasattr(TreeNode, 'func'):
    proc = rpr_getfp('ImGui_TreeNode')
    TreeNode.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = TreeNode.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

@reapy.inside_reaper()
def TreeNodeEx(ctx, str_id, label, flagsInOptional = None):
  if not hasattr(TreeNodeEx, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeEx')
    TreeNodeEx.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = TreeNodeEx.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

@reapy.inside_reaper()
def TreeNodeFlags_AllowItemOverlap():
  if not hasattr(TreeNodeFlags_AllowItemOverlap, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_AllowItemOverlap')
    TreeNodeFlags_AllowItemOverlap.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_AllowItemOverlap, 'cache'):
    TreeNodeFlags_AllowItemOverlap.cache = TreeNodeFlags_AllowItemOverlap.func()
  return TreeNodeFlags_AllowItemOverlap.cache

@reapy.inside_reaper()
def TreeNodeFlags_Bullet():
  if not hasattr(TreeNodeFlags_Bullet, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Bullet')
    TreeNodeFlags_Bullet.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_Bullet, 'cache'):
    TreeNodeFlags_Bullet.cache = TreeNodeFlags_Bullet.func()
  return TreeNodeFlags_Bullet.cache

@reapy.inside_reaper()
def TreeNodeFlags_CollapsingHeader():
  if not hasattr(TreeNodeFlags_CollapsingHeader, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_CollapsingHeader')
    TreeNodeFlags_CollapsingHeader.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_CollapsingHeader, 'cache'):
    TreeNodeFlags_CollapsingHeader.cache = TreeNodeFlags_CollapsingHeader.func()
  return TreeNodeFlags_CollapsingHeader.cache

@reapy.inside_reaper()
def TreeNodeFlags_DefaultOpen():
  if not hasattr(TreeNodeFlags_DefaultOpen, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_DefaultOpen')
    TreeNodeFlags_DefaultOpen.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_DefaultOpen, 'cache'):
    TreeNodeFlags_DefaultOpen.cache = TreeNodeFlags_DefaultOpen.func()
  return TreeNodeFlags_DefaultOpen.cache

@reapy.inside_reaper()
def TreeNodeFlags_FramePadding():
  if not hasattr(TreeNodeFlags_FramePadding, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_FramePadding')
    TreeNodeFlags_FramePadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_FramePadding, 'cache'):
    TreeNodeFlags_FramePadding.cache = TreeNodeFlags_FramePadding.func()
  return TreeNodeFlags_FramePadding.cache

@reapy.inside_reaper()
def TreeNodeFlags_Framed():
  if not hasattr(TreeNodeFlags_Framed, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Framed')
    TreeNodeFlags_Framed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_Framed, 'cache'):
    TreeNodeFlags_Framed.cache = TreeNodeFlags_Framed.func()
  return TreeNodeFlags_Framed.cache

@reapy.inside_reaper()
def TreeNodeFlags_Leaf():
  if not hasattr(TreeNodeFlags_Leaf, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Leaf')
    TreeNodeFlags_Leaf.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_Leaf, 'cache'):
    TreeNodeFlags_Leaf.cache = TreeNodeFlags_Leaf.func()
  return TreeNodeFlags_Leaf.cache

@reapy.inside_reaper()
def TreeNodeFlags_NoAutoOpenOnLog():
  if not hasattr(TreeNodeFlags_NoAutoOpenOnLog, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_NoAutoOpenOnLog')
    TreeNodeFlags_NoAutoOpenOnLog.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_NoAutoOpenOnLog, 'cache'):
    TreeNodeFlags_NoAutoOpenOnLog.cache = TreeNodeFlags_NoAutoOpenOnLog.func()
  return TreeNodeFlags_NoAutoOpenOnLog.cache

@reapy.inside_reaper()
def TreeNodeFlags_NoTreePushOnOpen():
  if not hasattr(TreeNodeFlags_NoTreePushOnOpen, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_NoTreePushOnOpen')
    TreeNodeFlags_NoTreePushOnOpen.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_NoTreePushOnOpen, 'cache'):
    TreeNodeFlags_NoTreePushOnOpen.cache = TreeNodeFlags_NoTreePushOnOpen.func()
  return TreeNodeFlags_NoTreePushOnOpen.cache

@reapy.inside_reaper()
def TreeNodeFlags_None():
  if not hasattr(TreeNodeFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_None')
    TreeNodeFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_None, 'cache'):
    TreeNodeFlags_None.cache = TreeNodeFlags_None.func()
  return TreeNodeFlags_None.cache

@reapy.inside_reaper()
def TreeNodeFlags_OpenOnArrow():
  if not hasattr(TreeNodeFlags_OpenOnArrow, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_OpenOnArrow')
    TreeNodeFlags_OpenOnArrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_OpenOnArrow, 'cache'):
    TreeNodeFlags_OpenOnArrow.cache = TreeNodeFlags_OpenOnArrow.func()
  return TreeNodeFlags_OpenOnArrow.cache

@reapy.inside_reaper()
def TreeNodeFlags_OpenOnDoubleClick():
  if not hasattr(TreeNodeFlags_OpenOnDoubleClick, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_OpenOnDoubleClick')
    TreeNodeFlags_OpenOnDoubleClick.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_OpenOnDoubleClick, 'cache'):
    TreeNodeFlags_OpenOnDoubleClick.cache = TreeNodeFlags_OpenOnDoubleClick.func()
  return TreeNodeFlags_OpenOnDoubleClick.cache

@reapy.inside_reaper()
def TreeNodeFlags_Selected():
  if not hasattr(TreeNodeFlags_Selected, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Selected')
    TreeNodeFlags_Selected.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_Selected, 'cache'):
    TreeNodeFlags_Selected.cache = TreeNodeFlags_Selected.func()
  return TreeNodeFlags_Selected.cache

@reapy.inside_reaper()
def TreeNodeFlags_SpanAvailWidth():
  if not hasattr(TreeNodeFlags_SpanAvailWidth, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_SpanAvailWidth')
    TreeNodeFlags_SpanAvailWidth.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_SpanAvailWidth, 'cache'):
    TreeNodeFlags_SpanAvailWidth.cache = TreeNodeFlags_SpanAvailWidth.func()
  return TreeNodeFlags_SpanAvailWidth.cache

@reapy.inside_reaper()
def TreeNodeFlags_SpanFullWidth():
  if not hasattr(TreeNodeFlags_SpanFullWidth, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_SpanFullWidth')
    TreeNodeFlags_SpanFullWidth.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(TreeNodeFlags_SpanFullWidth, 'cache'):
    TreeNodeFlags_SpanFullWidth.cache = TreeNodeFlags_SpanFullWidth.func()
  return TreeNodeFlags_SpanFullWidth.cache

@reapy.inside_reaper()
def TreePop(ctx):
  if not hasattr(TreePop, 'func'):
    proc = rpr_getfp('ImGui_TreePop')
    TreePop.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx),)
  TreePop.func(args[0])

@reapy.inside_reaper()
def TreePush(ctx, str_id):
  if not hasattr(TreePush, 'func'):
    proc = rpr_getfp('ImGui_TreePush')
    TreePush.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(str_id))
  TreePush.func(args[0], args[1])

@reapy.inside_reaper()
def Unindent(ctx, indent_wInOptional = None):
  if not hasattr(Unindent, 'func'):
    proc = rpr_getfp('ImGui_Unindent')
    Unindent.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), c_double(indent_wInOptional) if indent_wInOptional != None else None)
  Unindent.func(args[0], byref(args[1]) if args[1] != None else None)

@reapy.inside_reaper()
def VSliderDouble(ctx, label, size_w, size_h, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(VSliderDouble, 'func'):
    proc = rpr_getfp('ImGui_VSliderDouble')
    VSliderDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(size_w), c_double(size_h), c_double(vInOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = VSliderDouble.func(args[0], args[1], args[2], args[3], byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, float(args[4].value)

@reapy.inside_reaper()
def VSliderInt(ctx, label, size_w, size_h, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(VSliderInt, 'func'):
    proc = rpr_getfp('ImGui_VSliderInt')
    VSliderInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('Context*', ctx), rpr_packsc(label), c_double(size_w), c_double(size_h), c_int(vInOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = VSliderInt.func(args[0], args[1], args[2], args[3], byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, int(args[4].value)

@reapy.inside_reaper()
def ValidatePtr(pointer, type):
  if not hasattr(ValidatePtr, 'func'):
    proc = rpr_getfp('ImGui_ValidatePtr')
    ValidatePtr.func = CFUNCTYPE(c_bool, c_void_p, c_char_p)(proc)
  args = (rpr_packp('void*', pointer), rpr_packsc(type))
  rval = ValidatePtr.func(args[0], args[1])
  return rval

@reapy.inside_reaper()
def Viewport_GetCenter(viewport, xOut = None, yOut = None):
  if not hasattr(Viewport_GetCenter, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetCenter')
    Viewport_GetCenter.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Viewport*', viewport), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  Viewport_GetCenter.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def Viewport_GetPos(viewport, xOut = None, yOut = None):
  if not hasattr(Viewport_GetPos, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetPos')
    Viewport_GetPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Viewport*', viewport), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  Viewport_GetPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def Viewport_GetSize(viewport, wOut = None, hOut = None):
  if not hasattr(Viewport_GetSize, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetSize')
    Viewport_GetSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Viewport*', viewport), c_double(wOut if wOut != None else 0), c_double(hOut if hOut != None else 0))
  Viewport_GetSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def Viewport_GetWorkCenter(viewport, xOut = None, yOut = None):
  if not hasattr(Viewport_GetWorkCenter, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetWorkCenter')
    Viewport_GetWorkCenter.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Viewport*', viewport), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  Viewport_GetWorkCenter.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def Viewport_GetWorkPos(viewport, xOut = None, yOut = None):
  if not hasattr(Viewport_GetWorkPos, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetWorkPos')
    Viewport_GetWorkPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Viewport*', viewport), c_double(xOut if xOut != None else 0), c_double(yOut if yOut != None else 0))
  Viewport_GetWorkPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def Viewport_GetWorkSize(viewport, wOut = None, hOut = None):
  if not hasattr(Viewport_GetWorkSize, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetWorkSize')
    Viewport_GetWorkSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('Viewport*', viewport), c_double(wOut if wOut != None else 0), c_double(hOut if hOut != None else 0))
  Viewport_GetWorkSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

@reapy.inside_reaper()
def WindowFlags_AlwaysAutoResize():
  if not hasattr(WindowFlags_AlwaysAutoResize, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysAutoResize')
    WindowFlags_AlwaysAutoResize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_AlwaysAutoResize, 'cache'):
    WindowFlags_AlwaysAutoResize.cache = WindowFlags_AlwaysAutoResize.func()
  return WindowFlags_AlwaysAutoResize.cache

@reapy.inside_reaper()
def WindowFlags_AlwaysHorizontalScrollbar():
  if not hasattr(WindowFlags_AlwaysHorizontalScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysHorizontalScrollbar')
    WindowFlags_AlwaysHorizontalScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_AlwaysHorizontalScrollbar, 'cache'):
    WindowFlags_AlwaysHorizontalScrollbar.cache = WindowFlags_AlwaysHorizontalScrollbar.func()
  return WindowFlags_AlwaysHorizontalScrollbar.cache

@reapy.inside_reaper()
def WindowFlags_AlwaysUseWindowPadding():
  if not hasattr(WindowFlags_AlwaysUseWindowPadding, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysUseWindowPadding')
    WindowFlags_AlwaysUseWindowPadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_AlwaysUseWindowPadding, 'cache'):
    WindowFlags_AlwaysUseWindowPadding.cache = WindowFlags_AlwaysUseWindowPadding.func()
  return WindowFlags_AlwaysUseWindowPadding.cache

@reapy.inside_reaper()
def WindowFlags_AlwaysVerticalScrollbar():
  if not hasattr(WindowFlags_AlwaysVerticalScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysVerticalScrollbar')
    WindowFlags_AlwaysVerticalScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_AlwaysVerticalScrollbar, 'cache'):
    WindowFlags_AlwaysVerticalScrollbar.cache = WindowFlags_AlwaysVerticalScrollbar.func()
  return WindowFlags_AlwaysVerticalScrollbar.cache

@reapy.inside_reaper()
def WindowFlags_HorizontalScrollbar():
  if not hasattr(WindowFlags_HorizontalScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_HorizontalScrollbar')
    WindowFlags_HorizontalScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_HorizontalScrollbar, 'cache'):
    WindowFlags_HorizontalScrollbar.cache = WindowFlags_HorizontalScrollbar.func()
  return WindowFlags_HorizontalScrollbar.cache

@reapy.inside_reaper()
def WindowFlags_MenuBar():
  if not hasattr(WindowFlags_MenuBar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_MenuBar')
    WindowFlags_MenuBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_MenuBar, 'cache'):
    WindowFlags_MenuBar.cache = WindowFlags_MenuBar.func()
  return WindowFlags_MenuBar.cache

@reapy.inside_reaper()
def WindowFlags_NoBackground():
  if not hasattr(WindowFlags_NoBackground, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoBackground')
    WindowFlags_NoBackground.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoBackground, 'cache'):
    WindowFlags_NoBackground.cache = WindowFlags_NoBackground.func()
  return WindowFlags_NoBackground.cache

@reapy.inside_reaper()
def WindowFlags_NoCollapse():
  if not hasattr(WindowFlags_NoCollapse, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoCollapse')
    WindowFlags_NoCollapse.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoCollapse, 'cache'):
    WindowFlags_NoCollapse.cache = WindowFlags_NoCollapse.func()
  return WindowFlags_NoCollapse.cache

@reapy.inside_reaper()
def WindowFlags_NoDecoration():
  if not hasattr(WindowFlags_NoDecoration, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoDecoration')
    WindowFlags_NoDecoration.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoDecoration, 'cache'):
    WindowFlags_NoDecoration.cache = WindowFlags_NoDecoration.func()
  return WindowFlags_NoDecoration.cache

@reapy.inside_reaper()
def WindowFlags_NoDocking():
  if not hasattr(WindowFlags_NoDocking, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoDocking')
    WindowFlags_NoDocking.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoDocking, 'cache'):
    WindowFlags_NoDocking.cache = WindowFlags_NoDocking.func()
  return WindowFlags_NoDocking.cache

@reapy.inside_reaper()
def WindowFlags_NoFocusOnAppearing():
  if not hasattr(WindowFlags_NoFocusOnAppearing, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoFocusOnAppearing')
    WindowFlags_NoFocusOnAppearing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoFocusOnAppearing, 'cache'):
    WindowFlags_NoFocusOnAppearing.cache = WindowFlags_NoFocusOnAppearing.func()
  return WindowFlags_NoFocusOnAppearing.cache

@reapy.inside_reaper()
def WindowFlags_NoInputs():
  if not hasattr(WindowFlags_NoInputs, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoInputs')
    WindowFlags_NoInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoInputs, 'cache'):
    WindowFlags_NoInputs.cache = WindowFlags_NoInputs.func()
  return WindowFlags_NoInputs.cache

@reapy.inside_reaper()
def WindowFlags_NoMouseInputs():
  if not hasattr(WindowFlags_NoMouseInputs, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoMouseInputs')
    WindowFlags_NoMouseInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoMouseInputs, 'cache'):
    WindowFlags_NoMouseInputs.cache = WindowFlags_NoMouseInputs.func()
  return WindowFlags_NoMouseInputs.cache

@reapy.inside_reaper()
def WindowFlags_NoMove():
  if not hasattr(WindowFlags_NoMove, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoMove')
    WindowFlags_NoMove.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoMove, 'cache'):
    WindowFlags_NoMove.cache = WindowFlags_NoMove.func()
  return WindowFlags_NoMove.cache

@reapy.inside_reaper()
def WindowFlags_NoNav():
  if not hasattr(WindowFlags_NoNav, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoNav')
    WindowFlags_NoNav.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoNav, 'cache'):
    WindowFlags_NoNav.cache = WindowFlags_NoNav.func()
  return WindowFlags_NoNav.cache

@reapy.inside_reaper()
def WindowFlags_NoNavFocus():
  if not hasattr(WindowFlags_NoNavFocus, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoNavFocus')
    WindowFlags_NoNavFocus.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoNavFocus, 'cache'):
    WindowFlags_NoNavFocus.cache = WindowFlags_NoNavFocus.func()
  return WindowFlags_NoNavFocus.cache

@reapy.inside_reaper()
def WindowFlags_NoNavInputs():
  if not hasattr(WindowFlags_NoNavInputs, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoNavInputs')
    WindowFlags_NoNavInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoNavInputs, 'cache'):
    WindowFlags_NoNavInputs.cache = WindowFlags_NoNavInputs.func()
  return WindowFlags_NoNavInputs.cache

@reapy.inside_reaper()
def WindowFlags_NoResize():
  if not hasattr(WindowFlags_NoResize, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoResize')
    WindowFlags_NoResize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoResize, 'cache'):
    WindowFlags_NoResize.cache = WindowFlags_NoResize.func()
  return WindowFlags_NoResize.cache

@reapy.inside_reaper()
def WindowFlags_NoSavedSettings():
  if not hasattr(WindowFlags_NoSavedSettings, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoSavedSettings')
    WindowFlags_NoSavedSettings.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoSavedSettings, 'cache'):
    WindowFlags_NoSavedSettings.cache = WindowFlags_NoSavedSettings.func()
  return WindowFlags_NoSavedSettings.cache

@reapy.inside_reaper()
def WindowFlags_NoScrollWithMouse():
  if not hasattr(WindowFlags_NoScrollWithMouse, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoScrollWithMouse')
    WindowFlags_NoScrollWithMouse.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoScrollWithMouse, 'cache'):
    WindowFlags_NoScrollWithMouse.cache = WindowFlags_NoScrollWithMouse.func()
  return WindowFlags_NoScrollWithMouse.cache

@reapy.inside_reaper()
def WindowFlags_NoScrollbar():
  if not hasattr(WindowFlags_NoScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoScrollbar')
    WindowFlags_NoScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoScrollbar, 'cache'):
    WindowFlags_NoScrollbar.cache = WindowFlags_NoScrollbar.func()
  return WindowFlags_NoScrollbar.cache

@reapy.inside_reaper()
def WindowFlags_NoTitleBar():
  if not hasattr(WindowFlags_NoTitleBar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoTitleBar')
    WindowFlags_NoTitleBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_NoTitleBar, 'cache'):
    WindowFlags_NoTitleBar.cache = WindowFlags_NoTitleBar.func()
  return WindowFlags_NoTitleBar.cache

@reapy.inside_reaper()
def WindowFlags_None():
  if not hasattr(WindowFlags_None, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_None')
    WindowFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_None, 'cache'):
    WindowFlags_None.cache = WindowFlags_None.func()
  return WindowFlags_None.cache

@reapy.inside_reaper()
def WindowFlags_TopMost():
  if not hasattr(WindowFlags_TopMost, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_TopMost')
    WindowFlags_TopMost.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_TopMost, 'cache'):
    WindowFlags_TopMost.cache = WindowFlags_TopMost.func()
  return WindowFlags_TopMost.cache

@reapy.inside_reaper()
def WindowFlags_UnsavedDocument():
  if not hasattr(WindowFlags_UnsavedDocument, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_UnsavedDocument')
    WindowFlags_UnsavedDocument.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(WindowFlags_UnsavedDocument, 'cache'):
    WindowFlags_UnsavedDocument.cache = WindowFlags_UnsavedDocument.func()
  return WindowFlags_UnsavedDocument.cache
