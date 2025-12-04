import 'package:flutter/material.dart';

class TradeScreen extends StatelessWidget {
  const TradeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Trade Screen'),
      ),
      body: const Center(
        child: Text('Charts and orders will appear here (TradingView / WebView integration).'),
      ),
    );
  }
}
