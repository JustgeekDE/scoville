<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="7.4.0">
    <drawing>
        <settings>
            <setting alwaysvectorfont="yes"/>
            <setting verticaltext="up"/>
        </settings>
        <grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01"
              altunitdist="inch" altunit="inch"/>
        <layers>
            <layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
            <layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
            <layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
            <layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
            <layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
            <layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
            <layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
            <layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
            <layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
            <layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
            <layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
            <layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
            <layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
            <layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
            <layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
            <layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
            <layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
            <layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
            <layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
            <layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
            <layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
            <layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
            <layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
            <layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
            <layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
            <layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
            <layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
            <layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
            <layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
            <layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
            <layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
            <layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
            <layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
            <layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
            <layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
            <layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
            <layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
            <layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
            <layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
            <layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
            <layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
            <layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
            <layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
            <layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
            <layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
            <layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
        </layers>
        <schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
            <libraries>
                <library name="p.peter-leds">
                    <packages>
                        <package name="CHIPLED_0603">
                            <description>&lt;b&gt;CHIPLED&lt;/b&gt;&lt;p&gt;
                                Source: http://www.osram.convergy.de/ ... LG_LY Q971.pdf
                            </description>
                            <wire x1="-0.3" y1="0.8" x2="0.3" y2="0.8" width="0.1016" layer="51" curve="170.055574"/>
                            <wire x1="-0.275" y1="-0.825" x2="0.275" y2="-0.825" width="0.0508" layer="51"
                                  curve="-180"/>
                            <wire x1="-0.4" y1="0.375" x2="-0.4" y2="-0.35" width="0.1016" layer="51"/>
                            <wire x1="0.4" y1="0.35" x2="0.4" y2="-0.35" width="0.1016" layer="51"/>
                            <circle x="-0.35" y="0.625" radius="0.075" width="0.0508" layer="51"/>
                            <smd name="C" x="0" y="0.75" dx="0.8" dy="0.8" layer="1"/>
                            <smd name="A" x="0" y="-0.75" dx="0.8" dy="0.8" layer="1"/>
                            <text x="-0.635" y="-1.27" size="1.27" layer="25" rot="R90">&gt;NAME</text>
                            <text x="1.905" y="-1.27" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
                            <rectangle x1="-0.45" y1="0.7" x2="-0.25" y2="0.85" layer="51"/>
                            <rectangle x1="-0.275" y1="0.55" x2="-0.225" y2="0.6" layer="51"/>
                            <rectangle x1="-0.45" y1="0.35" x2="-0.4" y2="0.725" layer="51"/>
                            <rectangle x1="0.25" y1="0.55" x2="0.45" y2="0.85" layer="51"/>
                            <rectangle x1="-0.45" y1="0.35" x2="0.45" y2="0.575" layer="51"/>
                            <rectangle x1="-0.45" y1="-0.85" x2="-0.25" y2="-0.35" layer="51"/>
                            <rectangle x1="0.25" y1="-0.85" x2="0.45" y2="-0.35" layer="51"/>
                            <rectangle x1="-0.275" y1="-0.575" x2="0.275" y2="-0.35" layer="51"/>
                            <rectangle x1="-0.275" y1="-0.65" x2="-0.175" y2="-0.55" layer="51"/>
                            <rectangle x1="0.175" y1="-0.65" x2="0.275" y2="-0.55" layer="51"/>
                            <rectangle x1="-0.125" y1="0" x2="0.125" y2="0.24" layer="21"/>
                        </package>
                        <package name="CHIPLED_0805">
                            <description>&lt;b&gt;CHIPLED&lt;/b&gt;&lt;p&gt;
                                Source: http://www.osram.convergy.de/ ... LG_R971.pdf
                            </description>
                            <wire x1="-0.35" y1="0.925" x2="0.35" y2="0.925" width="0.1016" layer="51"
                                  curve="162.394521"/>
                            <wire x1="-0.35" y1="-0.925" x2="0.35" y2="-0.925" width="0.1016" layer="51"
                                  curve="-162.394521"/>
                            <wire x1="0.575" y1="0.525" x2="0.575" y2="-0.525" width="0.1016" layer="51"/>
                            <wire x1="-0.575" y1="-0.5" x2="-0.575" y2="0.925" width="0.1016" layer="51"/>
                            <circle x="-0.45" y="0.85" radius="0.103" width="0.1016" layer="51"/>
                            <smd name="C" x="0" y="1.05" dx="1.2" dy="1.2" layer="1"/>
                            <smd name="A" x="0" y="-1.05" dx="1.2" dy="1.2" layer="1"/>
                            <text x="-1.27" y="-1.27" size="1.27" layer="25" rot="R90">&gt;NAME</text>
                            <text x="2.54" y="-1.27" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
                            <rectangle x1="0.3" y1="0.5" x2="0.625" y2="1" layer="51"/>
                            <rectangle x1="-0.325" y1="0.5" x2="-0.175" y2="0.75" layer="51"/>
                            <rectangle x1="0.175" y1="0.5" x2="0.325" y2="0.75" layer="51"/>
                            <rectangle x1="-0.2" y1="0.5" x2="0.2" y2="0.675" layer="51"/>
                            <rectangle x1="0.3" y1="-1" x2="0.625" y2="-0.5" layer="51"/>
                            <rectangle x1="-0.625" y1="-1" x2="-0.3" y2="-0.5" layer="51"/>
                            <rectangle x1="0.175" y1="-0.75" x2="0.325" y2="-0.5" layer="51"/>
                            <rectangle x1="-0.325" y1="-0.75" x2="-0.175" y2="-0.5" layer="51"/>
                            <rectangle x1="-0.2" y1="-0.675" x2="0.2" y2="-0.5" layer="51"/>
                            <rectangle x1="-0.2" y1="0" x2="0.2" y2="0.3" layer="21"/>
                            <rectangle x1="-0.6" y1="0.5" x2="-0.3" y2="0.8" layer="51"/>
                            <rectangle x1="-0.625" y1="0.925" x2="-0.3" y2="1" layer="51"/>
                        </package>
                        <package name="CHIPLED_1206">
                            <description>&lt;b&gt;CHIPLED&lt;/b&gt;&lt;p&gt;
                                Source: http://www.osram.convergy.de/ ... LG_LY N971.pdf
                            </description>
                            <wire x1="-0.4" y1="1.6" x2="0.4" y2="1.6" width="0.1016" layer="51" curve="172.619069"/>
                            <wire x1="-0.8" y1="-0.95" x2="-0.8" y2="0.95" width="0.1016" layer="51"/>
                            <wire x1="0.8" y1="0.95" x2="0.8" y2="-0.95" width="0.1016" layer="51"/>
                            <circle x="-0.55" y="1.425" radius="0.1" width="0.1016" layer="51"/>
                            <smd name="C" x="0" y="1.75" dx="1.5" dy="1.5" layer="1"/>
                            <smd name="A" x="0" y="-1.75" dx="1.5" dy="1.5" layer="1"/>
                            <text x="-1.27" y="-1.27" size="1.27" layer="25" rot="R90">&gt;NAME</text>
                            <text x="2.54" y="-1.27" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
                            <rectangle x1="-0.85" y1="1.525" x2="-0.35" y2="1.65" layer="51"/>
                            <rectangle x1="-0.85" y1="1.225" x2="-0.625" y2="1.55" layer="51"/>
                            <rectangle x1="-0.45" y1="1.225" x2="-0.325" y2="1.45" layer="51"/>
                            <rectangle x1="-0.65" y1="1.225" x2="-0.225" y2="1.35" layer="51"/>
                            <rectangle x1="0.35" y1="1.3" x2="0.85" y2="1.65" layer="51"/>
                            <rectangle x1="0.25" y1="1.225" x2="0.85" y2="1.35" layer="51"/>
                            <rectangle x1="-0.85" y1="0.95" x2="0.85" y2="1.25" layer="51"/>
                            <rectangle x1="-0.85" y1="-1.65" x2="0.85" y2="-0.95" layer="51"/>
                            <rectangle x1="-0.85" y1="0.35" x2="-0.525" y2="0.775" layer="21"/>
                            <rectangle x1="0.525" y1="0.35" x2="0.85" y2="0.775" layer="21"/>
                            <rectangle x1="-0.175" y1="0" x2="0.175" y2="0.35" layer="21"/>
                        </package>
                        <package name="LED-3MM">
                            <description>&lt;B&gt;LED&lt;/B&gt;&lt;p&gt;
                                3 mm, round
                            </description>
                            <wire x1="1.5748" y1="-1.27" x2="1.5748" y2="1.27" width="0.254" layer="51"/>
                            <wire x1="-1.524" y1="0" x2="-1.1708" y2="0.9756" width="0.1524" layer="51"
                                  curve="-39.80361"/>
                            <wire x1="-1.524" y1="0" x2="-1.1391" y2="-1.0125" width="0.1524" layer="51"
                                  curve="41.633208"/>
                            <wire x1="1.1571" y1="0.9918" x2="1.524" y2="0" width="0.1524" layer="51"
                                  curve="-40.601165"/>
                            <wire x1="1.1708" y1="-0.9756" x2="1.524" y2="0" width="0.1524" layer="51"
                                  curve="39.80361"/>
                            <wire x1="0" y1="1.524" x2="1.2401" y2="0.8858" width="0.1524" layer="21"
                                  curve="-54.461337"/>
                            <wire x1="-1.2192" y1="0.9144" x2="0" y2="1.524" width="0.1524" layer="21"
                                  curve="-53.130102"/>
                            <wire x1="0" y1="-1.524" x2="1.203" y2="-0.9356" width="0.1524" layer="21"
                                  curve="52.126876"/>
                            <wire x1="-1.203" y1="-0.9356" x2="0" y2="-1.524" width="0.1524" layer="21"
                                  curve="52.126876"/>
                            <wire x1="-0.635" y1="0" x2="0" y2="0.635" width="0.1524" layer="51" curve="-90"/>
                            <wire x1="-1.016" y1="0" x2="0" y2="1.016" width="0.1524" layer="51" curve="-90"/>
                            <wire x1="0" y1="-0.635" x2="0.635" y2="0" width="0.1524" layer="51" curve="90"/>
                            <wire x1="0" y1="-1.016" x2="1.016" y2="0" width="0.1524" layer="51" curve="90"/>
                            <wire x1="0" y1="2.032" x2="1.561" y2="1.3009" width="0.254" layer="21" curve="-50.193108"/>
                            <wire x1="-1.7929" y1="0.9562" x2="0" y2="2.032" width="0.254" layer="21"
                                  curve="-61.926949"/>
                            <wire x1="0" y1="-2.032" x2="1.5512" y2="-1.3126" width="0.254" layer="21"
                                  curve="49.763022"/>
                            <wire x1="-1.7643" y1="-1.0082" x2="0" y2="-2.032" width="0.254" layer="21"
                                  curve="60.255215"/>
                            <wire x1="-2.032" y1="0" x2="-1.7891" y2="0.9634" width="0.254" layer="51"
                                  curve="-28.301701"/>
                            <wire x1="-2.032" y1="0" x2="-1.7306" y2="-1.065" width="0.254" layer="51"
                                  curve="31.60822"/>
                            <pad name="A" x="-1.27" y="0" drill="0.8128" shape="octagon"/>
                            <pad name="K" x="1.27" y="0" drill="0.8128" shape="octagon"/>
                            <text x="1.905" y="0.381" size="1.27" layer="25" ratio="10">&gt;NAME</text>
                            <text x="1.905" y="-1.651" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
                        </package>
                        <package name="LED-5MM">
                            <description>&lt;B&gt;LED&lt;/B&gt;&lt;p&gt;
                                5 mm, round
                            </description>
                            <wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.2032" layer="21"/>
                            <wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.254" layer="21"
                                  curve="-286.260205"/>
                            <wire x1="-1.143" y1="0" x2="0" y2="1.143" width="0.1524" layer="51" curve="-90"/>
                            <wire x1="0" y1="-1.143" x2="1.143" y2="0" width="0.1524" layer="51" curve="90"/>
                            <wire x1="-1.651" y1="0" x2="0" y2="1.651" width="0.1524" layer="51" curve="-90"/>
                            <wire x1="0" y1="-1.651" x2="1.651" y2="0" width="0.1524" layer="51" curve="90"/>
                            <wire x1="-2.159" y1="0" x2="0" y2="2.159" width="0.1524" layer="51" curve="-90"/>
                            <wire x1="0" y1="-2.159" x2="2.159" y2="0" width="0.1524" layer="51" curve="90"/>
                            <circle x="0" y="0" radius="2.54" width="0.1524" layer="21"/>
                            <pad name="A" x="-1.27" y="0" drill="0.8128" shape="octagon"/>
                            <pad name="K" x="1.27" y="0" drill="0.8128" shape="octagon"/>
                            <text x="3.175" y="0.5334" size="1.27" layer="25" ratio="10">&gt;NAME</text>
                            <text x="3.2004" y="-1.8034" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
                        </package>
                        <package name="LED-5MM-EDGE-OVAL">
                            <smd name="A" x="0" y="0" dx="1.5" dy="3.5" layer="1" roundness="100"/>
                            <smd name="K" x="0" y="0" dx="1.5" dy="3.5" layer="16" roundness="100"/>
                            <wire x1="0" y1="4.5" x2="-0.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="-0.5" y1="4.5" x2="-2.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="-2.5" y1="4.5" x2="-2.5" y2="9.5" width="0.127" layer="51"/>
                            <wire x1="2.5" y1="9.5" x2="2.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="2.5" y1="4.5" x2="0.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="0.5" y1="4.5" x2="0" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="2.5" y1="9.5" x2="0" y2="12" width="0.127" layer="51" curve="90"/>
                            <wire x1="0" y1="12" x2="-2.5" y2="9.5" width="0.127" layer="51" curve="90"/>
                            <wire x1="-0.5" y1="4.5" x2="-0.5" y2="-1.5" width="0.127" layer="51"/>
                            <wire x1="-0.5" y1="-1.5" x2="0.5" y2="-1.5" width="0.127" layer="51"/>
                            <wire x1="0.5" y1="-1.5" x2="0.5" y2="4.5" width="0.127" layer="51"/>
                            <text x="-1.5" y="-1.5" size="0.8" layer="25" rot="R90">&gt;NAME</text>
                            <text x="2" y="-1.5" size="0.8" layer="27" rot="R90">&gt;VALUE</text>
                            <wire x1="0" y1="4.5" x2="-0.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="-0.5" y1="4.5" x2="-2.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="-2.5" y1="4.5" x2="-2.5" y2="9.5" width="0.127" layer="52"/>
                            <wire x1="2.5" y1="9.5" x2="2.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="2.5" y1="4.5" x2="0.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="0.5" y1="4.5" x2="0" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="2.5" y1="9.5" x2="0" y2="12" width="0.127" layer="52" curve="90"/>
                            <wire x1="0" y1="12" x2="-2.5" y2="9.5" width="0.127" layer="52" curve="90"/>
                            <wire x1="-0.5" y1="4.5" x2="-0.5" y2="-1.5" width="0.127" layer="52"/>
                            <wire x1="-0.5" y1="-1.5" x2="0.5" y2="-1.5" width="0.127" layer="52"/>
                            <wire x1="0.5" y1="-1.5" x2="0.5" y2="4.5" width="0.127" layer="52"/>
                            <text x="2.5" y="-1.5" size="1.7" layer="52" rot="MR0">-</text>
                            <text x="1" y="-1.5" size="1.7" layer="51">+</text>
                        </package>
                        <package name="LED-EDGE-ROUND">
                            <smd name="A" x="0" y="0" dx="2" dy="2" layer="1" roundness="100"/>
                            <smd name="K" x="0" y="0" dx="2" dy="2" layer="16" roundness="100"/>
                            <wire x1="0" y1="4.5" x2="-0.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="-0.5" y1="4.5" x2="-2.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="-2.5" y1="4.5" x2="-2.5" y2="9.5" width="0.127" layer="51"/>
                            <wire x1="2.5" y1="9.5" x2="2.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="2.5" y1="4.5" x2="0.5" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="0.5" y1="4.5" x2="0" y2="4.5" width="0.127" layer="51"/>
                            <wire x1="2.5" y1="9.5" x2="0" y2="12" width="0.127" layer="51" curve="90"/>
                            <wire x1="0" y1="12" x2="-2.5" y2="9.5" width="0.127" layer="51" curve="90"/>
                            <wire x1="-0.5" y1="4.5" x2="-0.5" y2="-1.5" width="0.127" layer="51"/>
                            <wire x1="-0.5" y1="-1.5" x2="0.5" y2="-1.5" width="0.127" layer="51"/>
                            <wire x1="0.5" y1="-1.5" x2="0.5" y2="4.5" width="0.127" layer="51"/>
                            <text x="-1.5" y="-1.5" size="0.8" layer="25" rot="R90">&gt;NAME</text>
                            <text x="2" y="-1.5" size="0.8" layer="27" rot="R90">&gt;VALUE</text>
                            <wire x1="0" y1="4.5" x2="-0.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="-0.5" y1="4.5" x2="-2.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="-2.5" y1="4.5" x2="-2.5" y2="9.5" width="0.127" layer="52"/>
                            <wire x1="2.5" y1="9.5" x2="2.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="2.5" y1="4.5" x2="0.5" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="0.5" y1="4.5" x2="0" y2="4.5" width="0.127" layer="52"/>
                            <wire x1="2.5" y1="9.5" x2="0" y2="12" width="0.127" layer="52" curve="90"/>
                            <wire x1="0" y1="12" x2="-2.5" y2="9.5" width="0.127" layer="52" curve="90"/>
                            <wire x1="-0.5" y1="4.5" x2="-0.5" y2="-1.5" width="0.127" layer="52"/>
                            <wire x1="-0.5" y1="-1.5" x2="0.5" y2="-1.5" width="0.127" layer="52"/>
                            <wire x1="0.5" y1="-1.5" x2="0.5" y2="4.5" width="0.127" layer="52"/>
                            <text x="2.5" y="-1.5" size="1.7" layer="52" rot="MR0">-</text>
                            <text x="1" y="-1.5" size="1.7" layer="51">+</text>
                        </package>
                    </packages>
                    <symbols>
                        <symbol name="LED">
                            <wire x1="0" y1="1.397" x2="0" y2="0" width="0.254" layer="94"/>
                            <wire x1="0" y1="0" x2="0" y2="-1.397" width="0.254" layer="94"/>
                            <wire x1="0" y1="-1.397" x2="2.159" y2="0" width="0.254" layer="94"/>
                            <wire x1="2.159" y1="0" x2="0" y2="1.397" width="0.254" layer="94"/>
                            <pin name="A" x="-2.54" y="0" visible="off" length="short"/>
                            <pin name="C" x="5.08" y="0" visible="off" length="short" rot="R180"/>
                            <wire x1="2.54" y1="0" x2="2.159" y2="0" width="0.1524" layer="94"/>
                            <text x="0" y="2.794" size="1.27" layer="96">&gt;NAME</text>
                            <text x="0" y="-2.921" size="1.27" layer="96">&gt;VALUE</text>
                            <wire x1="2.159" y1="1.397" x2="2.159" y2="0" width="0.254" layer="94"/>
                            <wire x1="2.159" y1="0" x2="2.159" y2="-1.397" width="0.254" layer="94"/>
                            <wire x1="0.381" y1="1.651" x2="1.27" y2="2.54" width="0.127" layer="94"/>
                            <wire x1="1.27" y1="2.54" x2="0.762" y2="2.413" width="0.127" layer="94"/>
                            <wire x1="0.762" y1="2.413" x2="1.143" y2="2.032" width="0.127" layer="94"/>
                            <wire x1="1.143" y1="2.032" x2="1.27" y2="2.54" width="0.127" layer="94"/>
                            <wire x1="1.016" y1="1.143" x2="1.905" y2="2.032" width="0.127" layer="94"/>
                            <wire x1="1.905" y1="2.032" x2="1.397" y2="1.905" width="0.127" layer="94"/>
                            <wire x1="1.397" y1="1.905" x2="1.778" y2="1.524" width="0.127" layer="94"/>
                            <wire x1="1.778" y1="1.524" x2="1.905" y2="2.032" width="0.127" layer="94"/>
                        </symbol>
                    </symbols>
                    <devicesets>
                        <deviceset name="LED" prefix="L" uservalue="yes">
                            <gates>
                                <gate name="G$1" symbol="LED" x="0" y="0"/>
                            </gates>
                            <devices>
                                <device name="0603" package="CHIPLED_0603">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="C"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="0805" package="CHIPLED_0805">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="C"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="1206" package="CHIPLED_1206">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="C"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="3MM" package="LED-3MM">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="K"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="5MM" package="LED-5MM">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="K"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="EDGE-O" package="LED-5MM-EDGE-OVAL">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="K"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="EDGE-R" package="LED-EDGE-ROUND">
                                    <connects>
                                        <connect gate="G$1" pin="A" pad="A"/>
                                        <connect gate="G$1" pin="C" pad="K"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                            </devices>
                        </deviceset>
                    </devicesets>
                </library>
                <library name="p.peter-rcl">
                    <packages>
                        <package name="R0402">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="-0.245" y1="0.224" x2="0.245" y2="0.224" width="0.1524" layer="51"/>
                            <wire x1="0.245" y1="-0.224" x2="-0.245" y2="-0.224" width="0.1524" layer="51"/>
                            <wire x1="-1.473" y1="0.483" x2="1.473" y2="0.483" width="0.0508" layer="39"/>
                            <wire x1="1.473" y1="0.483" x2="1.473" y2="-0.483" width="0.0508" layer="39"/>
                            <wire x1="1.473" y1="-0.483" x2="-1.473" y2="-0.483" width="0.0508" layer="39"/>
                            <wire x1="-1.473" y1="-0.483" x2="-1.473" y2="0.483" width="0.0508" layer="39"/>
                            <smd name="1" x="-0.65" y="0" dx="0.7" dy="0.9" layer="1"/>
                            <smd name="2" x="0.65" y="0" dx="0.7" dy="0.9" layer="1"/>
                            <text x="-0.635" y="0.635" size="1.27" layer="25">&gt;NAME</text>
                            <text x="-0.635" y="-1.905" size="1.27" layer="27">&gt;VALUE</text>
                            <rectangle x1="-0.554" y1="-0.3048" x2="-0.254" y2="0.2951" layer="51"/>
                            <rectangle x1="0.2588" y1="-0.3048" x2="0.5588" y2="0.2951" layer="51"/>
                            <rectangle x1="-0.1999" y1="-0.4001" x2="0.1999" y2="0.4001" layer="35"/>
                        </package>
                        <package name="R0805">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;&lt;p&gt;</description>
                            <wire x1="-0.41" y1="0.635" x2="0.41" y2="0.635" width="0.1524" layer="51"/>
                            <wire x1="-0.41" y1="-0.635" x2="0.41" y2="-0.635" width="0.1524" layer="51"/>
                            <wire x1="-1.973" y1="0.983" x2="1.973" y2="0.983" width="0.0508" layer="39"/>
                            <wire x1="1.973" y1="0.983" x2="1.973" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="1.973" y1="-0.983" x2="-1.973" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="-1.973" y1="-0.983" x2="-1.973" y2="0.983" width="0.0508" layer="39"/>
                            <smd name="1" x="-0.95" y="0" dx="1.3" dy="1.5" layer="1"/>
                            <smd name="2" x="0.95" y="0" dx="1.3" dy="1.5" layer="1"/>
                            <text x="0" y="1.6" size="0.8" layer="25" font="fixed" ratio="12" align="center">&gt;NAME
                            </text>
                            <text x="0" y="-1.6" size="0.8" layer="27" font="vector" ratio="12" align="center">
                                &gt;VALUE
                            </text>
                            <rectangle x1="0.4064" y1="-0.6985" x2="1.0564" y2="0.7015" layer="51"/>
                            <rectangle x1="-1.0668" y1="-0.6985" x2="-0.4168" y2="0.7015" layer="51"/>
                            <rectangle x1="-0.1999" y1="-0.5001" x2="0.1999" y2="0.5001" layer="35"/>
                            <wire x1="-0.35" y1="0.93" x2="0.35" y2="0.93" width="0.15" layer="21"/>
                            <wire x1="-0.35" y1="-0.93" x2="0.35" y2="-0.93" width="0.15" layer="21"/>
                        </package>
                        <package name="R1005">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="-0.245" y1="0.224" x2="0.245" y2="0.224" width="0.1524" layer="51"/>
                            <wire x1="0.245" y1="-0.224" x2="-0.245" y2="-0.224" width="0.1524" layer="51"/>
                            <wire x1="-1.473" y1="0.483" x2="1.473" y2="0.483" width="0.0508" layer="39"/>
                            <wire x1="1.473" y1="0.483" x2="1.473" y2="-0.483" width="0.0508" layer="39"/>
                            <wire x1="1.473" y1="-0.483" x2="-1.473" y2="-0.483" width="0.0508" layer="39"/>
                            <wire x1="-1.473" y1="-0.483" x2="-1.473" y2="0.483" width="0.0508" layer="39"/>
                            <smd name="1" x="-0.65" y="0" dx="0.7" dy="0.9" layer="1"/>
                            <smd name="2" x="0.65" y="0" dx="0.7" dy="0.9" layer="1"/>
                            <text x="-0.635" y="0.635" size="1.27" layer="25">&gt;NAME</text>
                            <text x="-0.635" y="-1.905" size="1.27" layer="27">&gt;VALUE</text>
                            <rectangle x1="-0.554" y1="-0.3048" x2="-0.254" y2="0.2951" layer="51"/>
                            <rectangle x1="0.2588" y1="-0.3048" x2="0.5588" y2="0.2951" layer="51"/>
                            <rectangle x1="-0.1999" y1="-0.3" x2="0.1999" y2="0.3" layer="35"/>
                        </package>
                        <package name="R1206">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="0.9525" y1="-0.8128" x2="-0.9652" y2="-0.8128" width="0.1524" layer="51"/>
                            <wire x1="0.9525" y1="0.8128" x2="-0.9652" y2="0.8128" width="0.1524" layer="51"/>
                            <wire x1="-2.473" y1="0.983" x2="2.473" y2="0.983" width="0.0508" layer="39"/>
                            <wire x1="2.473" y1="0.983" x2="2.473" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="2.473" y1="-0.983" x2="-2.473" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="-2.473" y1="-0.983" x2="-2.473" y2="0.983" width="0.0508" layer="39"/>
                            <smd name="2" x="1.422" y="0" dx="1.6" dy="1.803" layer="1"/>
                            <smd name="1" x="-1.422" y="0" dx="1.6" dy="1.803" layer="1"/>
                            <text x="-1.27" y="1.27" size="1.27" layer="25">&gt;NAME</text>
                            <text x="-1.27" y="-2.54" size="1.27" layer="27">&gt;VALUE</text>
                            <rectangle x1="-1.6891" y1="-0.8763" x2="-0.9525" y2="0.8763" layer="51"/>
                            <rectangle x1="0.9525" y1="-0.8763" x2="1.6891" y2="0.8763" layer="51"/>
                            <rectangle x1="-0.3" y1="-0.7" x2="0.3" y2="0.7" layer="35"/>
                        </package>
                        <package name="R1210">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="-0.913" y1="1.219" x2="0.939" y2="1.219" width="0.1524" layer="51"/>
                            <wire x1="-0.913" y1="-1.219" x2="0.939" y2="-1.219" width="0.1524" layer="51"/>
                            <wire x1="-2.473" y1="1.483" x2="2.473" y2="1.483" width="0.0508" layer="39"/>
                            <wire x1="2.473" y1="1.483" x2="2.473" y2="-1.483" width="0.0508" layer="39"/>
                            <wire x1="2.473" y1="-1.483" x2="-2.473" y2="-1.483" width="0.0508" layer="39"/>
                            <wire x1="-2.473" y1="-1.483" x2="-2.473" y2="1.483" width="0.0508" layer="39"/>
                            <smd name="1" x="-1.4" y="0" dx="1.6" dy="2.7" layer="1"/>
                            <smd name="2" x="1.4" y="0" dx="1.6" dy="2.7" layer="1"/>
                            <text x="-2.54" y="1.905" size="1.27" layer="25">&gt;NAME</text>
                            <text x="-2.54" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
                            <rectangle x1="-1.651" y1="-1.3081" x2="-0.9009" y2="1.2918" layer="51"/>
                            <rectangle x1="0.9144" y1="-1.3081" x2="1.6645" y2="1.2918" layer="51"/>
                            <rectangle x1="-0.3" y1="-0.8999" x2="0.3" y2="0.8999" layer="35"/>
                        </package>
                        <package name="R2010">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="-1.662" y1="1.245" x2="1.662" y2="1.245" width="0.1524" layer="51"/>
                            <wire x1="-1.637" y1="-1.245" x2="1.687" y2="-1.245" width="0.1524" layer="51"/>
                            <wire x1="-3.473" y1="1.483" x2="3.473" y2="1.483" width="0.0508" layer="39"/>
                            <wire x1="3.473" y1="1.483" x2="3.473" y2="-1.483" width="0.0508" layer="39"/>
                            <wire x1="3.473" y1="-1.483" x2="-3.473" y2="-1.483" width="0.0508" layer="39"/>
                            <wire x1="-3.473" y1="-1.483" x2="-3.473" y2="1.483" width="0.0508" layer="39"/>
                            <smd name="1" x="-2.2" y="0" dx="1.8" dy="2.7" layer="1"/>
                            <smd name="2" x="2.2" y="0" dx="1.8" dy="2.7" layer="1"/>
                            <text x="-3.175" y="1.905" size="1.27" layer="25">&gt;NAME</text>
                            <text x="-3.175" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
                            <rectangle x1="-2.4892" y1="-1.3208" x2="-1.6393" y2="1.3292" layer="51"/>
                            <rectangle x1="1.651" y1="-1.3208" x2="2.5009" y2="1.3292" layer="51"/>
                        </package>
                        <package name="R2012">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="-0.41" y1="0.635" x2="0.41" y2="0.635" width="0.1524" layer="51"/>
                            <wire x1="-0.41" y1="-0.635" x2="0.41" y2="-0.635" width="0.1524" layer="51"/>
                            <wire x1="-1.973" y1="0.983" x2="1.973" y2="0.983" width="0.0508" layer="39"/>
                            <wire x1="1.973" y1="0.983" x2="1.973" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="1.973" y1="-0.983" x2="-1.973" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="-1.973" y1="-0.983" x2="-1.973" y2="0.983" width="0.0508" layer="39"/>
                            <smd name="1" x="-0.85" y="0" dx="1.3" dy="1.5" layer="1"/>
                            <smd name="2" x="0.85" y="0" dx="1.3" dy="1.5" layer="1"/>
                            <text x="-0.635" y="1.27" size="1.27" layer="25">&gt;NAME</text>
                            <text x="-0.635" y="-2.54" size="1.27" layer="27">&gt;VALUE</text>
                            <rectangle x1="0.4064" y1="-0.6985" x2="1.0564" y2="0.7015" layer="51"/>
                            <rectangle x1="-1.0668" y1="-0.6985" x2="-0.4168" y2="0.7015" layer="51"/>
                            <rectangle x1="-0.1001" y1="-0.5999" x2="0.1001" y2="0.5999" layer="35"/>
                        </package>
                        <package name="R0603">
                            <description>&lt;b&gt;RESISTOR&lt;/b&gt;</description>
                            <wire x1="-0.432" y1="-0.356" x2="0.432" y2="-0.356" width="0.1524" layer="51"/>
                            <wire x1="0.432" y1="0.356" x2="-0.432" y2="0.356" width="0.1524" layer="51"/>
                            <wire x1="-1.473" y1="0.983" x2="1.473" y2="0.983" width="0.0508" layer="39"/>
                            <wire x1="1.473" y1="0.983" x2="1.473" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="1.473" y1="-0.983" x2="-1.473" y2="-0.983" width="0.0508" layer="39"/>
                            <wire x1="-1.473" y1="-0.983" x2="-1.473" y2="0.983" width="0.0508" layer="39"/>
                            <smd name="1" x="-0.85" y="0" dx="1" dy="1.1" layer="1"/>
                            <smd name="2" x="0.85" y="0" dx="1" dy="1.1" layer="1"/>
                            <text x="0" y="1.6" size="0.8" layer="25" font="vector" ratio="12" rot="SR0" align="center">
                                &gt;NAME
                            </text>
                            <text x="0" y="-1.6" size="0.8" layer="27" font="vector" ratio="12" rot="SR0"
                                  align="center">&gt;VALUE
                            </text>
                            <rectangle x1="0.4318" y1="-0.4318" x2="0.8382" y2="0.4318" layer="51"/>
                            <rectangle x1="-0.8382" y1="-0.4318" x2="-0.4318" y2="0.4318" layer="51"/>
                            <rectangle x1="-0.1999" y1="-0.4001" x2="0.1999" y2="0.4001" layer="35"/>
                            <wire x1="-0.4" y1="0.73" x2="0.4" y2="0.73" width="0.15" layer="21"/>
                            <wire x1="-0.4" y1="-0.73" x2="0.4" y2="-0.73" width="0.15" layer="21"/>
                        </package>
                    </packages>
                    <symbols>
                        <symbol name="R-EU">
                            <wire x1="-2.54" y1="-0.889" x2="2.54" y2="-0.889" width="0.254" layer="94"/>
                            <wire x1="2.54" y1="0.889" x2="-2.54" y2="0.889" width="0.254" layer="94"/>
                            <wire x1="2.54" y1="-0.889" x2="2.54" y2="0.889" width="0.254" layer="94"/>
                            <wire x1="-2.54" y1="-0.889" x2="-2.54" y2="0.889" width="0.254" layer="94"/>
                            <text x="-3.81" y="1.4986" size="1.778" layer="95">&gt;NAME</text>
                            <text x="-3.81" y="-3.302" size="1.778" layer="96">&gt;VALUE</text>
                            <pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" swaplevel="1"
                                 rot="R180"/>
                            <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" swaplevel="1"/>
                        </symbol>
                    </symbols>
                    <devicesets>
                        <deviceset name="R-EU_" prefix="R" uservalue="yes">
                            <description>&lt;B&gt;RESISTOR&lt;/B&gt;, European symbol</description>
                            <gates>
                                <gate name="G$1" symbol="R-EU" x="0" y="0"/>
                            </gates>
                            <devices>
                                <device name="R0402" package="R0402">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R0603" package="R0603">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R0805" package="R0805">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R1005" package="R1005">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R1206" package="R1206">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R1210" package="R1210">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R2010" package="R2010">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                                <device name="R2012" package="R2012">
                                    <connects>
                                        <connect gate="G$1" pin="1" pad="1"/>
                                        <connect gate="G$1" pin="2" pad="2"/>
                                    </connects>
                                    <technologies>
                                        <technology name=""/>
                                    </technologies>
                                </device>
                            </devices>
                        </deviceset>
                    </devicesets>
                </library>
            </libraries>
            <attributes>
            </attributes>
            <variantdefs>
            </variantdefs>
            <classes>
                <class number="0" name="default" width="0" drill="0">
                </class>
            </classes>
            <parts>
                <part name="LED1" library="p.peter-leds" deviceset="LED" device="5MM"/>
                <part name="R1" library="p.peter-rcl" deviceset="R-EU_" device="R0805" value="1k"/>
            </parts>
            <sheets>
                <sheet>
                    <plain>
                        <wire x1="0" y1="12.7" x2="0" y2="0" width="0.1524" layer="97" style="shortdash"/>
                        <wire x1="0" y1="0" x2="25.4" y2="0" width="0.1524" layer="97" style="shortdash"/>
                        <wire x1="25.4" y1="0" x2="25.4" y2="12.7" width="0.1524" layer="97" style="shortdash"/>
                        <wire x1="25.4" y1="12.7" x2="0" y2="12.7" width="0.1524" layer="97" style="shortdash"/>
                        <text x="10.16" y="10.16" size="1.778" layer="97">LED</text>
                    </plain>
                    <instances>
                        <instance part="LED1" gate="G$1" x="17.78" y="5.08"/>
                        <instance part="R1" gate="G$1" x="7.62" y="5.08"/>
                    </instances>
                    <busses>
                    </busses>
                    <nets>
                        <net name="INT-1" class="0">
                            <segment>
                                <pinref part="LED1" gate="G$1" pin="A"/>
                                <wire x1="15.24" y1="5.08" x2="12.7" y2="5.08" width="0.1524" layer="91"/>
                                <pinref part="R1" gate="G$1" pin="2"/>
                            </segment>
                        </net>
                        <net name="CATHODE" class="0">
                            <segment>
                                <pinref part="LED1" gate="G$1" pin="C"/>
                                <wire x1="22.86" y1="5.08" x2="25.4" y2="5.08" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                        <net name="ANODE" class="0">
                            <segment>
                                <pinref part="R1" gate="G$1" pin="1"/>
                                <wire x1="2.54" y1="5.08" x2="0" y2="5.08" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                    </nets>
                </sheet>
            </sheets>
        </schematic>
    </drawing>
</eagle>
