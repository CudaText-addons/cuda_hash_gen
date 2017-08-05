from cudatext import *

class Command:

    def callback_btn_close(self, id_dlg, id_ctl, data='', info=''):
        dlg_proc(id_dlg, DLG_HIDE, 0)
        dlg_proc(id_dlg, DLG_FREE, 0)

    def callback_btn_file(self, id_dlg, id_ctl, data='', info=''):
        pass

    def callback_btn_copy(self, id_dlg, id_ctl, data='', info=''):
        pass

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

        n=dlg_proc(h, DLG_CTL_ADD, 'radio')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'chk_from_str', 'cap':'Calculate hash from &string:', 'x':6, 'y':40, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_from_str', 'x':6, 'y':65, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'radio')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'chk_from_file', 'cap':'Calculate hash from &file:', 'x':6, 'y':100, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_from_file', 'x':6, 'y':125, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_file', 'cap':'&Browse...', 'x':460, 'y':125, 'w':100,
          'on_change': self.callback_btn_file } )


        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'label_hash', 'cap':'Hash &value:', 'x':6, 'y':160, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_hash', 'x':6, 'y':180, 'w':450 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_close', 'cap':'&Copy', 'x':460, 'y':180, 'w':100,
          'on_change': self.callback_btn_copy } )


        n=dlg_proc(h, DLG_CTL_ADD, 'label')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'label_varify', 'cap':'&Enter hash to verify:', 'x':6, 'y':215, 'w':120 } )

        n=dlg_proc(h, DLG_CTL_ADD, 'edit')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'edit_verify', 'x':6, 'y':235, 'w':450 } )


        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_close', 'cap':'Close', 'x':460, 'y':290, 'w':100,
          'on_change': self.callback_btn_close } )

        return h

    def dialog(self):
        self.h_dlg = self.init_dlg()
        dlg_proc(self.h_dlg, DLG_SHOW_NONMODAL)

