package br.gov.caixa.peopi.utils;

import java.text.Format;
import java.util.Formatter;

/**
 * Classe utilitária no tratamento de strings
 * 
 * @author c071526
 *
 */
public class StringUtil {
	
	
	/**
	 * Adiciona zeros à esquerda de uma string de entrada
	 * 
	 * 
	 * @param entrada
	 * @param tamanho
	 * @return
	 */
	public static String adicionaEsquerda(String entrada, int tamanho){
		for (int i=entrada.length();(i<=tamanho);i++){
			entrada="0".concat(entrada);
		}
		return entrada;
	}
	
	/**
	 * @param entrada
	 * @param tamanho
	 * @return
	 */
	public static StringBuilder adicionaEspacos(StringBuilder entrada, int tamanho){
		if (!(entrada.length()<=tamanho)){
			entrada=entrada.append(" ");
		}
		return entrada;
	}
	
	

}
