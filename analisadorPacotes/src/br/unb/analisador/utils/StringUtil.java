package br.unb.analisador.utils;

import java.text.Format;
import java.util.Formatter;

/**
 * Classe utilit�ria no tratamento de strings
 * 
 * @author claudio
 *
 */
public class StringUtil {

	/**
	 * Adiciona zeros � esquerda de uma string de entrada
	 * 
	 * 
	 * @param entrada
	 * @param tamanho
	 * @return
	 */
	public static String adicionaEsquerda(String entrada, int tamanho) {
		for (int i = entrada.length(); (i <= tamanho); i++) {
			entrada = "0".concat(entrada);
		}
		return entrada;
	}

	/**
	 * Adiciona espaços em branco para corrigir o tamanho da string, de acordo
	 * com o parâmetro informado
	 * 
	 * @param entrada
	 * @param tamanho
	 * @return
	 */
	public static StringBuilder adicionaEspacos(StringBuilder entrada,
			int tamanho) {
		if (!(entrada.length() <= tamanho)) {
			entrada = entrada.append(" ");
		}
		return entrada;
	}

}
