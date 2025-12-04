import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class TradingService extends ChangeNotifier {
  bool isRunning = false;
  List<String> logs = [];
  Timer? _timer;

  final String backend = "http://127.0.0.1:5000"; // change when deploying

  void init() {
    _log("Service initialized");
  }

  void toggle() {
    isRunning = !isRunning;
    if (isRunning) start();
    else stop();
    notifyListeners();
  }

  void start() {
    _log("Bot started (demo)");
    _timer = Timer.periodic(const Duration(seconds: 8), (_) => _tick());
  }

  void stop() {
    _timer?.cancel();
    _timer = null;
    _log("Bot stopped");
    notifyListeners();
  }

  Future<void> _tick() async {
    try {
      final res = await http.post(Uri.parse("$backend/signal"), headers: {'Content-Type':'application/json'}, body: jsonEncode({'symbol':'BTCUSDT'})).timeout(const Duration(seconds: 6));
      if (res.statusCode == 200) {
        final map = jsonDecode(res.body);
        _log("Signal ${map['side']} entry ${map['entry']}");
        // here you can call connector to execute trade on exchange (demo only)
      } else {
        _log("Backend error ${res.statusCode}");
      }
    } catch (e) {
      _log("Tick error: $e");
    }
    notifyListeners();
  }

  void _log(String m) {
    logs.insert(0, "[${DateTime.now().toIso8601String()}] $m");
    if (logs.length > 500) logs.removeLast();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
}
