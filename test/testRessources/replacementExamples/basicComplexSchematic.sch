<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="7.4.0">
<drawing>
<settings>
<setting alwaysvectorfont="yes"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
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
<library name="supply1">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
                        GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
                        Please keep in mind, that these devices are necessary for the
                        automatic wiring of the supply signals.&lt;p&gt;
                        The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
                        In this library the device names are the same as the pin names of the symbols, therefore the
                        correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
                        &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
<symbol name="+5V">
<wire x1="1.27" y1="-1.905" x2="0" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="-1.27" y2="-1.905" width="0.254" layer="94"/>
<text x="-2.54" y="-5.08" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="+5V" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" prefix="GND">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="+5V" prefix="P+">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="+5V" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="p.peter-test">
<packages>
<package name="SIMPLE_LED">
<smd name="ANODE" x="1.27" y="3.81" dx="2.54" dy="0.635" layer="1"/>
<smd name="CATHODE" x="19.05" y="3.81" dx="2.54" dy="0.635" layer="1"/>
<wire x1="0" y1="0" x2="0" y2="3.81" width="0.127" layer="21"/>
<wire x1="0" y1="3.81" x2="0" y2="7.62" width="0.127" layer="21"/>
<wire x1="0" y1="7.62" x2="20.32" y2="7.62" width="0.127" layer="21"/>
<wire x1="20.32" y1="7.62" x2="20.32" y2="3.81" width="0.127" layer="21"/>
<wire x1="20.32" y1="3.81" x2="20.32" y2="0" width="0.127" layer="21"/>
<wire x1="20.32" y1="0" x2="0" y2="0" width="0.127" layer="21"/>
<wire x1="15.24" y1="3.81" x2="20.32" y2="3.81" width="0.127" layer="21"/>
<wire x1="2.54" y1="5.08" x2="2.54" y2="3.81" width="0.127" layer="21"/>
<wire x1="2.54" y1="3.81" x2="2.54" y2="2.54" width="0.127" layer="21"/>
<wire x1="2.54" y1="2.54" x2="8.89" y2="2.54" width="0.127" layer="21"/>
<wire x1="8.89" y1="2.54" x2="8.89" y2="3.81" width="0.127" layer="21"/>
<wire x1="8.89" y1="3.81" x2="8.89" y2="5.08" width="0.127" layer="21"/>
<wire x1="8.89" y1="5.08" x2="2.54" y2="5.08" width="0.127" layer="21"/>
<wire x1="12.7" y1="5.08" x2="12.7" y2="3.81" width="0.127" layer="21"/>
<wire x1="12.7" y1="3.81" x2="12.7" y2="2.54" width="0.127" layer="21"/>
<wire x1="12.7" y1="2.54" x2="15.24" y2="3.81" width="0.127" layer="21"/>
<wire x1="15.24" y1="3.81" x2="12.7" y2="5.08" width="0.127" layer="21"/>
<wire x1="0" y1="3.81" x2="2.54" y2="3.81" width="0.127" layer="21"/>
<wire x1="8.89" y1="3.81" x2="12.7" y2="3.81" width="0.127" layer="21"/>
<wire x1="13.97" y1="5.08" x2="15.24" y2="6.35" width="0.127" layer="21"/>
<wire x1="15.24" y1="6.35" x2="13.97" y2="6.35" width="0.127" layer="21"/>
<wire x1="13.97" y1="6.35" x2="15.24" y2="6.35" width="0.127" layer="21"/>
<wire x1="15.24" y1="6.35" x2="15.24" y2="5.08" width="0.127" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="LED-PACKAGE">
<wire x1="2.54" y1="0" x2="2.54" y2="5.08" width="0.254" layer="94"/>
<wire x1="2.54" y1="5.08" x2="2.54" y2="12.7" width="0.254" layer="94"/>
<wire x1="2.54" y1="12.7" x2="22.86" y2="12.7" width="0.254" layer="94"/>
<wire x1="22.86" y1="12.7" x2="22.86" y2="5.08" width="0.254" layer="94"/>
<wire x1="22.86" y1="5.08" x2="22.86" y2="0" width="0.254" layer="94"/>
<wire x1="22.86" y1="0" x2="2.54" y2="0" width="0.254" layer="94"/>
<pin name="ANODE" x="0" y="5.08" visible="off" length="short"/>
<pin name="CATHODE" x="25.4" y="5.08" visible="off" length="short" rot="R180"/>
<wire x1="2.54" y1="5.08" x2="5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="19.05" y1="5.08" x2="22.86" y2="5.08" width="0.254" layer="94"/>
<wire x1="5.08" y1="5.08" x2="5.08" y2="6.35" width="0.254" layer="94"/>
<wire x1="5.08" y1="6.35" x2="12.7" y2="6.35" width="0.254" layer="94"/>
<wire x1="12.7" y1="6.35" x2="12.7" y2="5.08" width="0.254" layer="94"/>
<wire x1="12.7" y1="5.08" x2="12.7" y2="3.81" width="0.254" layer="94"/>
<wire x1="12.7" y1="3.81" x2="5.08" y2="3.81" width="0.254" layer="94"/>
<wire x1="5.08" y1="3.81" x2="5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="16.51" y1="6.35" x2="19.05" y2="5.08" width="0.254" layer="94"/>
<wire x1="19.05" y1="5.08" x2="16.51" y2="3.81" width="0.254" layer="94"/>
<wire x1="16.51" y1="3.81" x2="16.51" y2="5.08" width="0.254" layer="94"/>
<wire x1="16.51" y1="5.08" x2="16.51" y2="6.35" width="0.254" layer="94"/>
<wire x1="19.05" y1="6.35" x2="19.05" y2="3.81" width="0.254" layer="94"/>
<wire x1="12.7" y1="5.08" x2="16.51" y2="5.08" width="0.254" layer="94"/>
<text x="2.54" y="13.208" size="1.778" layer="95">&gt;NAME</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="SIMPLE_LED">
<gates>
<gate name="G$1" symbol="LED-PACKAGE" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SIMPLE_LED">
<connects>
<connect gate="G$1" pin="ANODE" pad="ANODE"/>
<connect gate="G$1" pin="CATHODE" pad="CATHODE"/>
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
<part name="GND1" library="supply1" deviceset="GND" device=""/>
<part name="P+1" library="supply1" deviceset="+5V" device=""/>
<part name="P1" library="p.peter-test" deviceset="SIMPLE_LED" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="GND1" gate="1" x="27.94" y="0"/>
<instance part="P+1" gate="1" x="-2.54" y="10.16"/>
<instance part="P1" gate="G$1" x="0" y="0"/>
</instances>
<busses>
</busses>
<nets>
<net name="GND" class="0">
<segment>
<wire x1="25.4" y1="5.08" x2="27.94" y2="5.08" width="0.1524" layer="91"/>
<wire x1="27.94" y1="5.08" x2="27.94" y2="2.54" width="0.1524" layer="91"/>
<pinref part="GND1" gate="1" pin="GND"/>
<pinref part="P1" gate="G$1" pin="CATHODE"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<wire x1="0" y1="5.08" x2="-2.54" y2="5.08" width="0.1524" layer="91"/>
<wire x1="-2.54" y1="5.08" x2="-2.54" y2="7.62" width="0.1524" layer="91"/>
<pinref part="P+1" gate="1" pin="+5V"/>
<pinref part="P1" gate="G$1" pin="ANODE"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
