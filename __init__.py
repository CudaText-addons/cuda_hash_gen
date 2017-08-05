from cudatext import *

class Command:

    def calc(self, id_dlg, data, is_file):

        caption = '&Hash -- '+('file' if is_file else 'string')
        dlg_proc(id_dlg, DLG_CTL_PROP_SET, name='label_hash', prop={'cap': caption} )

        print('Hash from', ('file:' if is_file else 'string:'), repr(data) )


    def callback_btn_string(self, id_dlg, id_ctl, data='', info=''):

        prop = dlg_proc(id_dlg, DLG_CTL_PROP_GET, name='edit_string')
        s = prop['val']
        self.calc(id_dlg, s, False)


    def callback_btn_close(self, id_dlg, id_ctl, data='', info=''):

        dlg_proc(id_dlg, DLG_HIDE, 0)
        dlg_proc(id_dlg, DLG_FREE, 0)


    def callback_btn_file(self, id_dlg, id_ctl, data='', info=''):

        res = dlg_file(True, '', '', '')
        if res is None: return

        dlg_proc(id_dlg, DLG_CTL_PROP_SET, name='edit_file', prop={'val': res} )
        self.calc(id_dlg, res, True)


    def callback_btn_copy(self, id_dlg, id_ctl, data='', info=''):

        prop = dlg_proc(id_dlg, DLG_CTL_PROP_GET, name='edit_hash')
        s = prop['val']
        app_proc(PROC_SET_CLIP, s)
        msg_status('Hash copied to clipboard')


    def callback_btn_verify(self, id_dlg, id_ctl, data='', info=''):

        prop1 = dlg_proc(id_dlg, DLG_CTL_PROP_GET, name='edit_verify')
        prop2 = dlg_proc(id_dlg, DLG_CTL_PROP_GET, name='edit_hash')
        s1 = prop1['val']
        s2 = prop2['val']
        ok = bool(s1) and (s1==s2)

        caption = 'Verified' if ok else '?'
        dlg_proc(id_dlg, DLG_CTL_PROP_SET, name='label_verify_res', prop={'cap':caption} )


    def init_dlg(self):

        HASH_TYPES = ('MD4', 'MD5', 'SHA1')
        HASH_KIND = 1

        h=dlg_proc(0, DLG_CREATE)
        dlg_proc(h, DLG_PROP_SET, prop={'cap':'Hash Generator', 'w':570, 'h':320 })

        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'label_type', 'cap':'Hash &type:', 'x':6, 'y':10, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'combo_ro')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'combo_type', 'x':120, 'y':6, 'w':150,
          'items': '\t'.join(HASH_TYPES),
          'val': HASH_KIND } )

        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'chk_from_str', 'cap':'Calculate hash from &string:', 'x':6, 'y':40, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_string', 'x':6, 'y':60, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_string', 'cap':'C&alculate', 'x':460, 'y':60, 'w':100,
          'on_change': self.callback_btn_string } )


        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'chk_from_file', 'cap':'Calculate hash from &file:', 'x':6, 'y':95, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_file', 'props':(True,False,True), 'x':6, 'y':115, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_file', 'cap':'&Browse...', 'x':460, 'y':115, 'w':100,
          'on_change': self.callback_btn_file } )


        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'label_hash', 'cap':'&Hash value:', 'x':6, 'y':150, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_hash', 'props':(False,True,True), 'x':6, 'y':170, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_copy', 'cap':'&Copy', 'x':460, 'y':170, 'w':100,
          'on_change': self.callback_btn_copy } )


        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'label_varify', 'cap':'&Enter hash to verify:', 'x':6, 'y':205, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'label_verify_res', 'cap':'?', 'props':True, 'x':100, 'y':205, 'w':355 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_verify', 'props':(False,True,True), 'x':6, 'y':225, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_verify', 'cap':'&Verify', 'x':460, 'y':225, 'w':100,
          'on_change': self.callback_btn_verify } )


        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_close', 'cap':'Close', 'x':460, 'y':290, 'w':100,
          'on_change': self.callback_btn_close } )

        return h

    def dialog(self):
        self.h_dlg = self.init_dlg()
        dlg_proc(self.h_dlg, DLG_SHOW_NONMODAL)

