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
            <layer number="50" name="dxf" color="7" fill="1" visible="no" active="no"/>
            <layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
            <layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
            <layer number="53" name="tGND_GNDA" color="7" fill="9" visible="no" active="no"/>
            <layer number="54" name="bGND_GNDA" color="1" fill="9" visible="no" active="no"/>
            <layer number="56" name="wert" color="7" fill="1" visible="no" active="no"/>
            <layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
            <layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
            <layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
            <layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
            <layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
            <layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
            <layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
            <layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
            <layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
            <layer number="100" name="Muster" color="7" fill="1" visible="no" active="no"/>
            <layer number="101" name="Patch_Top" color="12" fill="4" visible="no" active="yes"/>
            <layer number="102" name="Vscore" color="7" fill="1" visible="no" active="yes"/>
            <layer number="103" name="fp3" color="7" fill="1" visible="no" active="yes"/>
            <layer number="104" name="Name" color="7" fill="1" visible="no" active="yes"/>
            <layer number="105" name="Beschreib" color="9" fill="1" visible="no" active="yes"/>
            <layer number="106" name="BGA-Top" color="4" fill="1" visible="no" active="yes"/>
            <layer number="107" name="BD-Top" color="5" fill="1" visible="no" active="yes"/>
            <layer number="108" name="fp8" color="7" fill="1" visible="no" active="yes"/>
            <layer number="109" name="fp9" color="7" fill="1" visible="no" active="yes"/>
            <layer number="110" name="fp0" color="7" fill="1" visible="no" active="yes"/>
            <layer number="116" name="Patch_BOT" color="9" fill="4" visible="no" active="yes"/>
            <layer number="121" name="_tsilk" color="7" fill="1" visible="no" active="yes"/>
            <layer number="122" name="_bsilk" color="7" fill="1" visible="no" active="yes"/>
            <layer number="123" name="tTestmark" color="7" fill="1" visible="no" active="yes"/>
            <layer number="124" name="bTestmark" color="7" fill="1" visible="no" active="yes"/>
            <layer number="125" name="_tNames" color="7" fill="1" visible="no" active="yes"/>
            <layer number="131" name="tAdjust" color="7" fill="1" visible="no" active="yes"/>
            <layer number="132" name="bAdjust" color="7" fill="1" visible="no" active="yes"/>
            <layer number="144" name="Drill_legend" color="7" fill="1" visible="no" active="yes"/>
            <layer number="151" name="HeatSink" color="7" fill="1" visible="no" active="yes"/>
            <layer number="199" name="Contour" color="7" fill="1" visible="no" active="yes"/>
            <layer number="200" name="200bmp" color="1" fill="10" visible="no" active="yes"/>
            <layer number="201" name="201bmp" color="2" fill="1" visible="no" active="no"/>
            <layer number="202" name="202bmp" color="3" fill="1" visible="no" active="no"/>
            <layer number="203" name="203bmp" color="4" fill="10" visible="no" active="yes"/>
            <layer number="204" name="204bmp" color="5" fill="10" visible="no" active="yes"/>
            <layer number="205" name="205bmp" color="6" fill="10" visible="no" active="yes"/>
            <layer number="206" name="206bmp" color="7" fill="10" visible="no" active="yes"/>
            <layer number="207" name="207bmp" color="8" fill="10" visible="no" active="yes"/>
            <layer number="208" name="208bmp" color="9" fill="10" visible="no" active="yes"/>
            <layer number="209" name="209bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="210" name="210bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="211" name="211bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="212" name="212bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="213" name="213bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="214" name="214bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="215" name="215bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="216" name="216bmp" color="7" fill="1" visible="no" active="yes"/>
            <layer number="217" name="217bmp" color="18" fill="1" visible="no" active="no"/>
            <layer number="218" name="218bmp" color="19" fill="1" visible="no" active="no"/>
            <layer number="219" name="219bmp" color="20" fill="1" visible="no" active="no"/>
            <layer number="220" name="220bmp" color="21" fill="1" visible="no" active="no"/>
            <layer number="221" name="221bmp" color="22" fill="1" visible="no" active="no"/>
            <layer number="222" name="222bmp" color="23" fill="1" visible="no" active="no"/>
            <layer number="223" name="223bmp" color="24" fill="1" visible="no" active="no"/>
            <layer number="224" name="224bmp" color="25" fill="1" visible="no" active="no"/>
            <layer number="250" name="Descript" color="7" fill="1" visible="no" active="no"/>
            <layer number="251" name="SMDround" color="7" fill="1" visible="no" active="no"/>
            <layer number="254" name="cooling" color="7" fill="1" visible="no" active="yes"/>
        </layers>
        <schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
            <libraries>
                <library name="p.peter-scoville.tests">
                    <packages>
                        <package name="RELAY-FINDER-40.51">
                            <pad name="N-" x="0" y="0" drill="1.5"/>
                            <pad name="CENTER" x="20" y="0" drill="1.5"/>
                            <pad name="NCL" x="15" y="7.5" drill="1.5"/>
                            <pad name="NOP" x="25" y="7.5" drill="1.5"/>
                            <wire x1="-3" y1="-2.5" x2="26" y2="-2.5" width="0.127" layer="51"/>
                            <wire x1="26" y1="-2.5" x2="26" y2="10" width="0.127" layer="51"/>
                            <wire x1="26" y1="10" x2="-3" y2="10" width="0.127" layer="51"/>
                            <wire x1="-3" y1="10" x2="-3" y2="-2.5" width="0.127" layer="51"/>
                            <pad name="N+" x="0" y="7.5" drill="1.5"/>
                        </package>
                    </packages>
                    <symbols>
                        <symbol name="RELAY">
                            <wire x1="-10.16" y1="5.08" x2="2.54" y2="5.08" width="0.254" layer="94"/>
                            <wire x1="2.54" y1="5.08" x2="7.62" y2="5.08" width="0.254" layer="94"/>
                            <wire x1="7.62" y1="5.08" x2="7.62" y2="0" width="0.254" layer="94"/>
                            <wire x1="7.62" y1="0" x2="7.62" y2="-5.08" width="0.254" layer="94"/>
                            <wire x1="7.62" y1="-5.08" x2="2.54" y2="-5.08" width="0.254" layer="94"/>
                            <wire x1="2.54" y1="-5.08" x2="-10.16" y2="-5.08" width="0.254" layer="94"/>
                            <wire x1="-10.16" y1="-5.08" x2="-10.16" y2="-2.54" width="0.254" layer="94"/>
                            <pin name="N+" x="-12.7" y="2.54" visible="off" length="short"/>
                            <pin name="N-" x="-12.7" y="-2.54" visible="off" length="short"/>
                            <pin name="NCL" x="2.54" y="7.62" visible="off" length="short" rot="R270"/>
                            <pin name="NOP" x="2.54" y="-7.62" visible="off" length="short" rot="R90"/>
                            <pin name="CENTER" x="10.16" y="0" visible="off" length="short" rot="R180"/>
                            <wire x1="-10.16" y1="-2.54" x2="-10.16" y2="2.54" width="0.254" layer="94"/>
                            <wire x1="-10.16" y1="2.54" x2="-10.16" y2="5.08" width="0.254" layer="94"/>
                            <wire x1="2.54" y1="-5.08" x2="2.54" y2="-2.54" width="0.254" layer="94"/>
                            <wire x1="2.54" y1="5.08" x2="2.54" y2="2.54" width="0.254" layer="94"/>
                            <wire x1="7.62" y1="0" x2="5.08" y2="0" width="0.254" layer="94"/>
                            <wire x1="5.08" y1="0" x2="0" y2="2.54" width="0.254" layer="94"/>
                            <circle x="2.54" y="2.54" radius="0.254" width="0.254" layer="94"/>
                            <circle x="2.54" y="-2.54" radius="0.254" width="0.254" layer="94"/>
                            <wire x1="-10.16" y1="2.54" x2="-5.08" y2="2.54" width="0.254" layer="94"/>
                            <wire x1="-10.16" y1="-2.54" x2="-5.08" y2="-2.54" width="0.254" layer="94"/>
                            <wire x1="-5.08" y1="-2.54" x2="-5.08" y2="-2.032" width="0.254" layer="94"/>
                            <wire x1="-5.08" y1="2.54" x2="-5.08" y2="2.032" width="0.254" layer="94"/>
                            <wire x1="-5.08" y1="2.032" x2="-5.08" y2="2.54" width="0.254" layer="94"/>
                            <wire x1="-5.08" y1="2.032" x2="-5.842" y2="2.032" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="2.032" x2="-5.842" y2="1.778" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="1.778" x2="-5.842" y2="1.016" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="1.016" x2="-5.842" y2="0.254" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="0.254" x2="-5.842" y2="-0.508" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="-0.508" x2="-5.842" y2="-1.27" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="-1.27" x2="-5.842" y2="-2.032" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="-2.032" x2="-4.318" y2="-2.032" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="-2.032" x2="-4.318" y2="-1.524" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="-1.524" x2="-4.318" y2="-0.762" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="-0.762" x2="-4.318" y2="0" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="0" x2="-4.318" y2="0.762" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="0.762" x2="-4.318" y2="1.524" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="1.524" x2="-4.318" y2="2.032" width="0.254" layer="94"/>
                            <wire x1="-4.318" y1="2.032" x2="-5.08" y2="2.032" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="1.016" x2="-4.318" y2="1.524" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="0.254" x2="-4.318" y2="0.762" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="-0.508" x2="-4.318" y2="0" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="-1.27" x2="-4.318" y2="-0.762" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="-2.032" x2="-4.318" y2="-1.524" width="0.254" layer="94"/>
                            <wire x1="-5.842" y1="1.778" x2="-5.08" y2="2.032" width="0.254" layer="94"/>
                            <text x="-10.16" y="5.588" size="1.27" layer="95">&gt;NAME</text>
                            <text x="-10.16" y="-6.858" size="1.27" layer="96">&gt;VALUE</text>
                        </symbol>
                    </symbols>
                    <devicesets>
                        <deviceset name="RELAY-GENERIC" uservalue="yes">
                            <gates>
                                <gate name="G$1" symbol="RELAY" x="15.24" y="0"/>
                            </gates>
                            <devices>
                                <device name="" package="RELAY-FINDER-40.51">
                                    <connects>
                                        <connect gate="G$1" pin="CENTER" pad="CENTER"/>
                                        <connect gate="G$1" pin="N+" pad="N+"/>
                                        <connect gate="G$1" pin="N-" pad="N-"/>
                                        <connect gate="G$1" pin="NCL" pad="NCL"/>
                                        <connect gate="G$1" pin="NOP" pad="NOP"/>
                                    </connects>
                                    <technologies>
                                        <technology name="">
                                            <attribute name="SV_SPICE_ORDER" value="NOP;CENTER;NCL;N+;N-"/>
                                            <attribute name="SV_SPICE_PREFIX" value="x"/>
                                            <attribute name="SV_SPICE_SUBCKT"
                                                       value=".subckt %NAME%  1   2   3   4   5\nSOpen 1 2 4 5 SW_OPEN on\nSClosed 2 3 4 5 SW_CLOSED on\n.model SW_OPEN SW(Ron=.1 Roff=1Meg Vt=6 )\n.model SW_CLOSED SW(Ron=1Meg Roff=.1 Vt=6 )\n.ends"/>
                                        </technology>
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
                <part name="RELAY1" library="p.peter-scoville.tests" deviceset="RELAY-GENERIC" device=""
                      value="basicRelay"/>
            </parts>
            <sheets>
                <sheet>
                    <plain>
                    </plain>
                    <instances>
                        <instance part="RELAY1" gate="G$1" x="58.42" y="43.18"/>
                    </instances>
                    <busses>
                    </busses>
                    <nets>
                        <net name="NPOS" class="0">
                            <segment>
                                <pinref part="RELAY1" gate="G$1" pin="N+"/>
                                <wire x1="45.72" y1="45.72" x2="43.18" y2="45.72" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                        <net name="NNEG" class="0">
                            <segment>
                                <pinref part="RELAY1" gate="G$1" pin="N-"/>
                                <wire x1="45.72" y1="40.64" x2="43.18" y2="40.64" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                        <net name="NCL" class="0">
                            <segment>
                                <pinref part="RELAY1" gate="G$1" pin="NCL"/>
                                <wire x1="60.96" y1="50.8" x2="60.96" y2="53.34" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                        <net name="CENT" class="0">
                            <segment>
                                <pinref part="RELAY1" gate="G$1" pin="CENTER"/>
                                <wire x1="68.58" y1="43.18" x2="71.12" y2="43.18" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                        <net name="NOP" class="0">
                            <segment>
                                <pinref part="RELAY1" gate="G$1" pin="NOP"/>
                                <wire x1="60.96" y1="35.56" x2="60.96" y2="33.02" width="0.1524" layer="91"/>
                            </segment>
                        </net>
                    </nets>
                </sheet>
            </sheets>
        </schematic>
    </drawing>
</eagle>
