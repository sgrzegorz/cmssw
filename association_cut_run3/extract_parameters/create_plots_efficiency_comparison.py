from ROOT import *


def draw(c,tree, tree1):
    
    gStyle.SetOptStat(0); # turn off statistics tab


    tree.SetTitle(f"{number_protons} proton(s) acc/exp")

    tree.Draw()

    tree1.SetLineColor( 2 )

    tree1.Draw("same")

    c.Update()

inp = TFile.Open("3rms.root")

inp1 = TFile.Open("4rms.root")





c = TCanvas('c af', '', 2000, 800)




c.Divide(1,2)

c_arm0 = c.cd(1)
c_arm0.SetTitle("arm0")

c_arm0.Divide(4,1)

number_protons = 1
for i in range(1,5):
    
    histpath = f"arm0/{number_protons}/p_eff_vs_xi"
    tree = inp.Get(histpath)
    tree1 = inp1.Get(histpath)

    c_sub = c_arm0.cd(i)
    draw(c_sub,tree,tree1)
    number_protons+=1





c_arm1 = c.cd(2)
c_arm1.Divide(4,1)

number_protons = 1
for i in range(1,5):
    
    histpath = f"arm0/{number_protons}/p_eff_vs_xi"
    tree = inp.Get(histpath)
    tree1 = inp1.Get(histpath)

    c_sub = c_arm1.cd(i)
    draw(c_sub,tree,tree1)
    number_protons+=1



legend = TLegend(0.5,0.2,0.8,0.4)
legend.AddEntry(tree,"3 RMS","L")
legend.AddEntry(tree1,"4 RMS","L")
legend.Draw()
c.Update()


c.cd()
newpad=TPad("newpad","a transparent pad",0,0,1,1)
newpad.Draw()
newpad.cd()
newpad.SetFillStyle(4000)
caption= TLatex()
caption.SetTextSize(0.025)
caption.DrawLatex(0.001,0.78,"arm0")
caption.DrawLatex(0.001,0.27,"arm1")

newpad.Update()



input("Press Enter to continue...")

