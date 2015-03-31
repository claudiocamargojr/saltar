package br.unb.analisador.servlet;

import br.unb.analisador.io.Arquivo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import java.util.logging.*;

/**
 * Servlet que realiza o upload de arquivos atrav[es do 
 * 
 * @author claudio
 *
 */
@WebServlet({ "/upload" })
@MultipartConfig
public class uploadFile extends HttpServlet {
	private static FileHandler fh;
	private static Logger logger = Logger.getLogger("br.gov.caixa.peopi.servlet");
	
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
	}

	protected void doPost(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		
		Part file = request.getPart("inputFile");
		long tamanhoArquivo = file.getSize();

		String filename = getFilename(file);
		
		InputStream filecontent = file.getInputStream();

		Arquivo.criarDiretorioDestino(); //Cria o diretorio de destino para gravacao do arquivo

		Arquivo a = new Arquivo();
		
		//Determinar aqui o local de gravacao do arquivo que esta sendo submetido a upload
		//a.(filecontent, "C://Desenvolvimento//" + filename
		//		, tamanhoArquivo);

		response.setContentType("text/plain");
		response.setCharacterEncoding("UTF-8");

		PrintWriter writer = response.getWriter();
		writer.write("O arquivo contendo dados de captura de rede <b>"
				+ "C:\\Desenvolvimento\\" + filename
				+ "</b> foi analisado com sucesso\n");
		writer.close();

		response.setHeader("Content-Type", "text/plain");
		response.setHeader("success", "yes");
	}

	private static String getFilename(Part part) {
		for (String cd : part.getHeader("content-disposition").split(";")) {
			if (cd.trim().startsWith("filename")) {
				String filename = cd.substring(cd.indexOf('=') + 1).trim()
						.replace("\"", "");
				return filename.substring(filename.lastIndexOf('/') + 1)
						.substring(filename.lastIndexOf('\\') + 1);
			}
		}
		return null;
	}

	private static String getValue(Part part) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(
				part.getInputStream(), "UTF-8"));
		StringBuilder value = new StringBuilder();
		char[] buffer = new char[1024];
		for (int length = 0; (length = reader.read(buffer)) > 0;) {
			value.append(buffer, 0, length);
		}
		return value.toString();
	}



}
