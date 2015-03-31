package br.unb.analisador.io;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.logging.*;

import org.apache.juli.logging.Log;

/**
 * @author Claudio
 *
 */
public class Arquivo {



	/**
	 * Fecha o arquivo em uso pelo processo
	 * 
	 * @param out
	 */
	static void closeQuietly(FileOutputStream out) {
		try {
			out.flush();
			out.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}



	/**
	 * Cria diret�rio de destino para os arquivos gerados de massa de testes
	 * 
	 */
	public static void criarDiretorioDestino() {
		File theDir = new File("Desenvolvimento");
		if (!theDir.exists()) {
			logger.log(Level.INFO, "creating directory: " + theDir.getName());
			boolean result = false;
			try {
				theDir.mkdir();
				result = true;
			} catch (SecurityException se) {
				se.printStackTrace();
			}
			if (result) {
				logger.log(Level.INFO, "Diret�rio criado");
			}
		}
	}

	/**
	 * Conta a quantidade de linhas do arquivo
	 * 
	 * @param arquivo
	 * @return
	 */
	private int countLines(InputStream arquivo) {
		LineNumberReader lineCounter = new LineNumberReader(
				new InputStreamReader(arquivo));
		String nextLine = null;

		try {
			while ((nextLine = lineCounter.readLine()) != null) {
				if (nextLine == null)
					break;
			}
			logger.log(Level.INFO, "Quantidade de linhas totais no arquivo: "
					+ lineCounter.getLineNumber());

		} catch (Exception e) {
			logger.log(Level.SEVERE, "N�o foi poss�vel contar a quantidade de linhas do arquivo.");
		}

		return lineCounter.getLineNumber();
	}


}
