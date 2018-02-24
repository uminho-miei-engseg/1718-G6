# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateBlindData-app.py
#
# Cripto-7.1.1 - Commmad line app to exemplify the usage of blindData
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that receives Data and pRDashComponents from STDIN and writes
blindMessage and blindComponents and pRComponents to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python generateBlindData-app.py -msg mensagem -RDash prDash")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    else:
        main()

def showResults(errorCode, result):
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("\n--- Blind message ---\n%s" % blindM)
        file = open("requerente.txt", "w")
        file.write(blindComponents)
        file.write("\n")
        file.write(pRComponents)
        file.close()
        print("\n--- Componentes guardadas em ficheiro ---\n")
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main():
    data = sys.argv[2]
    pRDashComponents = sys.argv[4]
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
