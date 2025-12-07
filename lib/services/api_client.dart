import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiClient {
  final String baseUrl;
  ApiClient(this.baseUrl);

  Future<Map<String,dynamic>> postSignal(String symbol) async {
    final res = await http.post(Uri.parse('$baseUrl/signal'),
        headers: {'Content-Type':'application/json'},
        body: jsonEncode({'symbol': symbol}));
    if (res.statusCode == 200) {
      return Map<String,dynamic>.from(jsonDecode(res.body));
    } else {
      return {'error':'status ${res.statusCode}'};
    }
  }
}
