#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Sep 08, 2020 09:30:28 PM +0430  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop74 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    menu .pop75 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    menu .pop76 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 

proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 766x450+324+142
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(pr,guicomplement_color)]
    ttk::notebook $top.tNo72 \
        -width 752 -height 436 -takefocus {} 
    vTcl:DefineAlias "$top.tNo72" "TNotebook1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.tNo72.t0 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo72.t0" "TNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo72 add $top.tNo72.t0 \
        -padding 0 -sticky nsew -state normal -text {Page 1} -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo72.t0
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.tBu73 \
        -takefocus {} -text Tbutton 
    vTcl:DefineAlias "$site_4_0.tBu73" "TButton1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.tBu73 \
        -in $site_4_0 -x 0 -relx 0.175 -y 0 -rely 0.124 -height 28 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.tNo72.t1 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo72.t1" "TNotebook1_t2" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo72 add $top.tNo72.t1 \
        -padding 0 -sticky nsew -state normal -text {Page 2} -image {} \
        -compound left -underline -1 
    set site_4_1  $top.tNo72.t1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo72 \
        -in $top -x 0 -relx 0.013 -y 0 -rely 0.022 -width 0 -relwidth 0.974 \
        -height 0 -relheight 0.953 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
