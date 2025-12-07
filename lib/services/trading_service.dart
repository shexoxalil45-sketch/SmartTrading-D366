import 'dart:async';
import 'package:flutter/foundation.dart';
import 'api_client.dart';

class TradingService extends ChangeNotifier {
  bool isRunning = false;
  List<String> logs = [];
  Timer? _timer;
  late ApiClient api;

  void init({String backend = 'http://127.0.0.1:5000'}) {
    api = ApiClient(backend);
    _log('Service initialized (backend: $backend)');
  }

  void toggle() {
    if (isRunning) stop();
    else start();
    notifyListeners();
  }

  void start() {
    if (isRunning) return;
    isRunning = true;
    _log('Bot started');
    _timer = Timer.periodic(const Duration(seconds: 10), (_) async {
      try {
        final sig = await api.postSignal('BTCUSDT');
        _log('Signal: ${sig['side']} entry:${sig['entry']}');
      } catch (e) {
        _log('Error: $e');
      }
      notifyListeners();
    });
    notifyListeners();
  }

  void stop() {
    _timer?.cancel();
    _timer = null;
    isRunning = false;
    _log('Bot stopped');
    notifyListeners();
  }

  void _log(String s) {
    logs.insert(0, '[${DateTime.now().toIso8601String()}] $s');
    if (logs.length > 500) logs.removeLast();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
}
