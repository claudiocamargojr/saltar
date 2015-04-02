package br.unb.analisador.protocols;


import java.io.IOException;

import org.jnetpcap.Pcap;
import org.jnetpcap.packet.JPacket;
import org.jnetpcap.packet.JPacketHandler;
import org.jnetpcap.packet.PcapPacket;
import org.jnetpcap.protocol.lan.Ethernet;
import org.jnetpcap.protocol.network.Ip4;

public class ExtractProtocolo {    

        private final StringBuilder errbuf = new StringBuilder(); // for any error messages
        Pcap pcap;
        Ip4 ip;
        
        public ExtractProtocolo(String originFilePath){
            System.out.println("Antes");    
            ip = new Ip4(); // Preallocate a IP header             
                     
            Pcap pcap = Pcap.openOffline(originFilePath, errbuf); 
            
            if (pcap == null) { 
                System.err.printf("Error while opening file : " + errbuf.toString()); 
                //throw new IOException("Could not open file: " + originFilePath); 
            }  
            
        }
                
        public void extractIp(){
            JPacketHandler<String> ipHandler = new JPacketHandler<String>() { 
                @Override
                public void nextPacket(JPacket packet, String user) {
                    Ethernet ether = new Ethernet();
                    if (packet.hasHeader(ip)) {
                        System.out.println("[" + packet.getFrameNumber() + "]");
                    }
                }
               
            };
            
            try {  
                
                pcap.loop(-1, ipHandler, "");
            } finally {  
                pcap.close();  
            }            
        }    
        

}

