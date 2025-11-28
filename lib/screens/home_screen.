import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:webview_flutter/webview_flutter.dart';

class HomeScreen extends StatefulWidget {
  final void Function(Locale) onLocaleChange;
  HomeScreen({required this.onLocaleChange});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String _langCode = 'en';
  Map<String, dynamic> _strings = {};

  @override
  void initState() {
    super.initState();
    _loadLang(_langCode);
  }

  Future<void> _loadLang(String code) async {
    final raw = await rootBundle.loadString('assets/lang/$code.json');
    setState(() {
      _strings = json.decode(raw);
      _langCode = code;
      widget.onLocaleChange(Locale(code.split('-').first));
    });
  }

  @override
  Widget build(BuildContext context) {
    final title = _strings['app_title'] ?? 'SmartTrading-D366';
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
        actions: [
          PopupMenuButton<String>(
            onSelected: (v) => _loadLang(v),
            itemBuilder: (_) => [
              PopupMenuItem(value: 'en.json', child: Text('English')),
              PopupMenuItem(value: 'ar.json', child: Text('العربية')),
              PopupMenuItem(value: 'de.json', child: Text('Deutsch')),
              PopupMenuItem(value: 'tr.json', child: Text('Türkçe')),
              PopupMenuItem(value: 'ku-k.json', child: Text('Kurmanji')),
              PopupMenuItem(value: 'ku-s.json', child: Text('Sorani')),
            ],
            icon: Icon(Icons.language),
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: WebView(
              initialUrl: 'https://your-backend-url-or-github-pages', // عدل حسبك
              javascriptMode: JavascriptMode.unrestricted,
            ),
          ),
          Container(
            padding: EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(child: Text(_strings['footer_text'] ?? 'Live charts powered')),
                ElevatedButton(
                  onPressed: () {
                    // مثال: action
                  },
                  child: Text(_strings['btn_open'] ?? 'Open'),
                )
              ],
            ),
          )
        ],
      ),
    );
  }
}
