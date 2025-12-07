import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class TradeScreen extends StatefulWidget {
  const TradeScreen({super.key});
  @override
  State<TradeScreen> createState() => _TradeScreenState();
}

class _TradeScreenState extends State<TradeScreen> {
  final String initialUrl = 'about:blank'; // later: TradingView widget or backend dashboard

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Trade / Chart')),
      body: const Center(child: Text('TradingView / Chart will be embedded here using WebView')),
    );
  }
}
